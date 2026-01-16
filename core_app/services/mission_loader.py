# core_app/services/mission_loader.py

from core_app.schemas.missione_schema import MissioniSchema
from engine_core.missions.gestore import GestoreMissioni
import os, json

def carica_missioni(directory="static/mission") -> GestoreMissioni:
    schema = MissioniSchema()
    missioni = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data = json.load(file)
                missioni += schema.load(data)  # carica tutte

    gm = GestoreMissioni()
    gm.lista_missioni = missioni
    return gm
