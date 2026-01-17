# tests/test_items.py

def test_pozione_cura_valore(sample_oggetti):
    poz = sample_oggetti["poz"]
    effetto = poz.usa(mod_ambiente=0)
    assert effetto == poz.valore

def test_bomba_acida_valore(sample_oggetti):
    bomba = sample_oggetti["bomba"]
    danno = bomba.usa()
    assert danno < 0

def test_medaglione_boost(sample_oggetti):
    med = sample_oggetti["med"]
    mod = med.usa()
    assert mod == med.valore
