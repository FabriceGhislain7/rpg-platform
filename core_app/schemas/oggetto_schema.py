import uuid
from marshmallow import Schema, fields, post_load, ValidationError
from engine_core.items.oggetto import Oggetto, PozioneCura, BombaAcida, Medaglione


def get_all_subclasses(cls):
    """
    Ritorna tutte le sottoclassi (anche indirette) di una classe.
    Utile per la deserializzazione dinamica.
    """
    subclasses = set()
    for subclass in cls.__subclasses__():
        subclasses.add(subclass)
        subclasses.update(get_all_subclasses(subclass))
    return subclasses


class OggettoSchema(Schema):
    """
    Schema Marshmallow per deserializzare oggetti di gioco in base
    al campo 'classe'.
    """
    id = fields.UUID(load_default=uuid.uuid4)
    nome = fields.Str(required=True)
    usato = fields.Bool(load_default=False)
    valore = fields.Int(load_default=30)
    tipo_oggetto = fields.Str()
    classe = fields.Str(required=True)

    @post_load
    def make_oggetto(self, data, **_kwargs):
        """
        Dopo il caricamento dei dati, crea un'istanza della sottoclasse corretta.
        """
        classe_nome = data.get("classe")
        if not classe_nome:
            raise ValidationError("'classe' è obbligatorio per istanziare l'oggetto.")

        oggetti_map = {
            cls.__name__: cls
            for cls in get_all_subclasses(Oggetto)
        }

        oggetto_cls = oggetti_map.get(classe_nome, Oggetto)

        # Rimuove 'classe' dai dati prima di passare al costruttore
        data_clean = {k: v for k, v in data.items() if k != "classe"}

        return oggetto_cls(**data_clean)
