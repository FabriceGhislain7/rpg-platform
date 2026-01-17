# tests/test_environment.py

def test_foresta_attacco(ambienti, sample_personaggi):
    foresta = ambienti["foresta"]
    mod = foresta.modifica_attacco(sample_personaggi["guerriero"])
    assert mod == foresta.mod_attacco

def test_vulcano_effetto_bomba(ambienti, sample_oggetti):
    vulcano = ambienti["vulcano"]
    bonus = vulcano.modifica_effetto_oggetto(sample_oggetti["bomba"])
    assert isinstance(bonus, int)

def test_palude_riduce_pozione(ambienti, sample_oggetti):
    palude = ambienti["palude"]
    rid = palude.modifica_effetto_oggetto(sample_oggetti["poz"])
    assert isinstance(rid, int)
