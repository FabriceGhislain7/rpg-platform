# tests/test_inventory.py

import uuid

def test_aggiungi_e_cerca(sample_oggetti, inventario_player):
    inv = inventario_player
    obj = sample_oggetti["poz"]
    inv.aggiungi_oggetto(obj)
    assert inv.cerca_oggetto(obj) is True

def test_usa_oggetto_rimuove(sample_oggetti, inventario_player):
    inv = inventario_player
    obj = sample_oggetti["bomba"]
    inv.aggiungi_oggetto(obj)
    result = inv.usa_oggetto(obj)
    assert result is not None
    assert obj not in inv.oggetti

def test_rimuovi_oggetto_per_id(sample_oggetti, inventario_player):
    inv = inventario_player
    obj = sample_oggetti["poz"]
    inv.aggiungi_oggetto(obj)
    removed = inv.rimuovi_oggetto(obj.id)
    assert removed is obj
