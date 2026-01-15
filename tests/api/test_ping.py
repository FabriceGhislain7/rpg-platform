from flask import Flask
import pytest

from core_app.api.ping_api import ping_blueprint
from core_app import create_flask_app