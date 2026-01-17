# tests/test_characters/test_personaggio.py

import pytest
from engine_core.characters.personaggio import Personaggio

def test_personaggio_base():
    p = Personaggio(nome="Test", classe="Generic")
    assert isinstance(p.id, object)  # uuid is set
    assert p.salute == 100
    assert p.salute_max == 200
