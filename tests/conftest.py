# tests/conftest.py

import uuid
import pytest

from engine_core.characters.classi import Mago, Guerriero, Ladro
from engine_core.items.oggetto import PozioneCura, BombaAcida, Medaglione
from engine_core.inventory.inventario import Inventario
from engine_core.environment.ambiente import Foresta, Vulcano, Palude
from engine_core.logic.strategy import Aggressiva, Difensiva, Equilibrata

@pytest.fixture
def sample_personaggi():
    return {
        "mago": Mago(nome="MagoTest"),
        "guerriero": Guerriero(nome="GuerrieroTest"),
        "ladro": Ladro(nome="LadroTest"),
    }

@pytest.fixture
def sample_oggetti():
    return {
        "poz": PozioneCura(),
        "bomba": BombaAcida(),
        "med": Medaglione(),
    }

@pytest.fixture
def inventario_player():
    inv = Inventario(id_proprietario=uuid.uuid4())
    return inv

@pytest.fixture
def ambienti():
    return {
        "foresta": Foresta(),
        "vulcano": Vulcano(),
        "palude": Palude(),
    }

@pytest.fixture
def strategie():
    return {
        "agg": Aggressiva(),
        "dif": Difensiva(),
        "eq": Equilibrata(),
    }
