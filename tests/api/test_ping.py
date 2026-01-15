import pytest
from flask import Flask

from core_app.factory import create_app


@pytest.fixture
def app() -> Flask:
    """
    Crea un'app Flask configurata per i test.
    """
    app = create_app()
    app.config.update({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    """
    Client di test per effettuare richieste HTTP simulate.
    """
    return app.test_client()


def test_ping_endpoint(client):
    """
    Verifica che /api/ping_url risponda correttamente.
    """
    response = client.get("/api/ping_url")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "message": "RPG Platform is running",
        "status": "ok"
    }