# engine_core/schemas/strategy_schema.py

from marshmallow import Schema, fields, post_load
from engine_core.logic.strategy import StrategiaFactory


class StrategiaSchema(Schema):
    """
    Schema per serializzare/deserializzare strategie NPC.
    """
    nome = fields.Str(required=True)

    @post_load
    def make_strategia(self, data, **kwargs):
        return StrategiaFactory.usa_strategia(data['nome'])
