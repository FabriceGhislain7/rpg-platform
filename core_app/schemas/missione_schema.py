import uuid
from marshmallow import Schema, fields, post_load
from engine_core.missions.missione import Missione
from core_app.schemas.ambiente_schema import AmbienteSchema
from core_app.schemas.personaggio_schema import PersonaggioSchema
from core_app.schemas.oggetto_schema import OggettoSchema
from core_app.schemas.strategy_schema import StrategiaSchema

class MissioneSchema(Schema):
    id = fields.UUID(required=True)
    ambiente = fields.Nested(AmbienteSchema, required=True)
    nemici = fields.List(fields.Nested(PersonaggioSchema), required=True)
    premi = fields.List(fields.Nested(OggettoSchema), required=True)
    nome = fields.Str(required=True)
    strategia_nemici = fields.Nested(StrategiaSchema, required=True)
    completata = fields.Bool(load_default=False)
    attiva = fields.Bool(load_default=False)

    @post_load
    def make_missione(self, data, **kwargs):
        return Missione(**data)


class MissioniSchema(Schema):
    """
    Per caricare più missioni da una lista
    """
    missioni = fields.List(fields.Nested(MissioneSchema))

    @post_load
    def make_lista(self, data, **kwargs):
        return data['missioni']
