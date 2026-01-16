import os
import json
from engine_core.missions.gestore import GestoreMissioni
from core_app.schemas.missione_schema import MissioniSchema

def carica_missioni(directory: str = "static/mission") -> GestoreMissioni:
    schema = MissioniSchema()
    missioni = []

    for file in os.listdir(directory):
        if file.endswith(".json"):
            with open(os.path.join(directory, file), 'r') as f:
                data = json.load(f)
                missioni += schema.load(data)

    gestore = GestoreMissioni()
    gestore.lista_missioni = missioni
    return gestore
