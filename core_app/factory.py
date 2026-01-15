from flask import Flask
from dotenv import load_dotenv
from config import Config


def create_app() -> Flask:
    """
    Crea e configura l'applicazione Flask per l'ambiente corrente.
    Carica eventuali variabili da file .env e registra i blueprint API.
    """
    load_dotenv()  # Carica variabili d'ambiente da .env, se presente

    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrazione dei blueprint API
    from core_app.api.ping_api import ping_blueprint
    app.register_blueprint(ping_blueprint, url_prefix="/api")

    return app
