import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Configurazione globale dell'applicazione Flask.
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    DATA_DIR = os.path.join(BASE_DIR, "data")
    os.makedirs(DATA_DIR, exist_ok=True)
    
    