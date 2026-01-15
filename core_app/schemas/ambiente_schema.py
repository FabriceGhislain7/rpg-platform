# rpg-platform/core_app/schemas/ambiente_schema.py

from marshmallow import Schema, fields, post_load
from engine_core.environment.ambiente import Ambiente


def get_all_subclasses(cls):
    subclasses = set()
    for subclass in cls.__subclasses__():
        subclasses.add(subclass)
    return subclasses


class AmbienteSchema(Schema):
    classe = fields.String(required=True)
    nome = fields.String(required=True)
    mod_attacco = fields.Integer()
    mod_cura = fields.Float()

    @post_load
    def make_obj(self, data, **kwargs):
        classe_nome = data.get("classe")
        ambienti_map = {
            subcls.__name__: subcls
            for subcls in get_all_subclasses(Ambiente)
        }
        data_clean = {k: v for k, v in data.items() if k != 'classe'}
        ambiente_cls = ambienti_map.get(classe_nome, Ambiente)
        return ambiente_cls(**data_clean)

    def dump(self, obj, *, many=None, **kwargs):
        data = super().dump(obj, many=many, **kwargs)
        if many:
            for i, item in enumerate(data):
                item['classe'] = obj[i].__class__.__name__
        else:
            data['classe'] = obj.__class__.__name__
        return data
