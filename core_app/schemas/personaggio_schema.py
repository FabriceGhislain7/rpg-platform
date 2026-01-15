# rpg-platform/core_app/schemas/personaggio_schema.py

import uuid
from marshmallow import Schema, fields, post_load, ValidationError
from engine_core.characters.personaggio import Personaggio
from engine_core.characters.classi import Mago, Guerriero, Ladro

def get_all_subclasses(cls):
    """
    Ritorna tutte le sottoclassi dirette di una classe.
    """
    return cls.__subclasses__()


class PersonaggioSchema(Schema):
    """
    Schema Marshmallow per serializzare e deserializzare oggetti Personaggio
    e relative sottoclassi (Mago, Guerriero, Ladro), usando il campo 'classe'
    come discriminatore.
    """
    # Campi comuni
    classe = fields.String(required=True)  # es: "Mago", "Guerriero", ecc.
    id = fields.UUID(load_default=uuid.uuid4)
    nome = fields.String(required=True)
    npc = fields.Boolean(load_default=True)
    salute_max = fields.Integer()
    salute = fields.Integer()
    attacco_min = fields.Integer()
    attacco_max = fields.Integer()
    livello = fields.Integer(load_default=1)
    destrezza = fields.Integer(load_default=15)
    storico_danni_subiti = fields.List(fields.Integer(), load_default=list)

    @post_load
    def make_personaggio(self, data, **_kwargs):
        """
        Dopo il caricamento dei dati, crea l'istanza corretta
        (Mago, Guerriero, Ladro, o Personaggio base) in base a 'classe'.
        """
        classe_nome = data.get("classe")
        if not classe_nome:
            raise ValidationError("'classe' è obbligatorio per istanziare il personaggio.")

        # Costruzione dinamica: classe -> oggetto Python
        classe_map = {
            cls.__name__: cls
            for cls in get_all_subclasses(Personaggio)
        }

        # Se la classe non è riconosciuta, fallback a Personaggio
        personaggio_cls = classe_map.get(classe_nome, Personaggio)

        # Rimozione del campo 'classe' dai kwargs del costruttore
        data_clean = {k: v for k, v in data.items() if k != "classe"}

        return personaggio_cls(**data_clean)
