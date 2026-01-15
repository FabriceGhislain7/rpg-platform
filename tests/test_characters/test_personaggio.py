from engine_core.characters.personaggio import Personaggio

def test_attacco_generato():
    pg = Personaggio(nome="Zoro", classe="Gueriero")
    danno = pg.attacca()
    
    assert isinstance(danno, int)
    assert danno >= 0
    assert danno <= pg.attacco_max + 10

