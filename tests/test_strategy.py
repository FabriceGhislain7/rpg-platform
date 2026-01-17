# tests/test_strategy.py

def test_aggressiva_uso_inventario(inventario_player, strategie, sample_oggetti):
    inv = inventario_player
    inv.aggiungi_oggetto(sample_oggetti["bomba"])
    result = strategie["agg"].uso_inventario_npc(100, inv)
    assert result is None or isinstance(result, int)

def test_difensiva_uso_inventario(inventario_player, strategie, sample_oggetti):
    inv = inventario_player
    inv.aggiungi_oggetto(sample_oggetti["poz"])
    result = strategie["dif"].uso_inventario_npc(30, inv)
    assert result is None or isinstance(result, int)

def test_equilibrata_uso_inventario(inventario_player, strategie, sample_oggetti):
    inv = inventario_player
    inv.aggiungi_oggetto(sample_oggetti["poz"])
    res = strategie["eq"].uso_inventario_npc(10, inv)
    assert res is None or isinstance(res, int)
