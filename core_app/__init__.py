from flask import Flask
from dotenv import load_dotenv
from config import Config

def create_flask_app():
    """
    Crea e configura l'applicazione Flask
    """
    load_dotenv()

    # Costruisco e configuro l'app
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    # Regisratrazione dei moduli API
    from core_app.api.ping_api import ping_blueprint
    flask_app.register_blueprint(ping_blueprint, url_prefix="/api")
    
    return flask_app
