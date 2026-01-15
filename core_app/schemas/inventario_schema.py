# rpg-platform/core_app/schemas/inventario_schema.py

import uuid
from marshmallow import Schema, fields, post_load, EXCLUDE
from engine_core.inventory.inventario import Inventario
from core_app.schemas.oggetto_schema import OggettoSchema


class InventarioSchema(Schema):
    """
    Schema Marshmallow per la serializzazione/deserializzazione
    degli inventari. Ricostruisce un oggetto Inventario a partire
    da JSON o dizionari Python.
    """
    class Meta:
        unknown = EXCLUDE  # Ignora i campi non dichiarati

    id = fields.UUID(required=True)
    id_proprietario = fields.UUID(allow_none=True)
    oggetti = fields.List(fields.Nested(OggettoSchema), load_default=list)

    @post_load
    def make_inventario(self, data, **kwargs):
        return Inventario(**data)
