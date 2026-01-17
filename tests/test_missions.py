# tests/test_missions.py

import uuid
from engine_core.missions.missione import Missione
from engine_core.characters.classi import Ladro, Guerriero, Mago
from engine_core.items.oggetto import PozioneCura
from engine_core.inventory.inventario import Inventario

def test_missione_verifica():
    missione = Missione(nome="TestMission")
    nemico = Ladro(nome="Goblin")
    missione.nemici.append(nemico)
    assert missione.verifica_completamento() is False

def test_missione_assegna_premio():
    missione = Missione(premi=[PozioneCura()])
    inv = Inventario(id_proprietario=uuid.uuid4())
    missione.assegna_premio([inv], "Player")
    assert len(inv.oggetti) == 1
