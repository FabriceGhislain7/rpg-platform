# core_app/factory.py

from flask import Flask
from dotenv import load_dotenv
from config import Config

def create_app() -> Flask:
    """
    Crea e configura l'app Flask.
    """
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrazione dei blueprint API
    from core_app.api.ping_api import ping_blueprint
    app.register_blueprint(ping_blueprint, url_prefix="/api")

    return app
