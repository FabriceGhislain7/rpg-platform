from flask import Blueprint, jsonify

gioco_blueprint = Blueprint("gioco_api", __name__)

@gioco_blueprint.route("/gioco/home", methods=["GET"])
def home():
    return jsonify({
        "title": "Benvenuto nel GDR Web App",
        "cta": "Vai al Menu Principale",
        "links": {
            "menu": "/gioco/menu",
            "about": "/gioco/about",
            "guide": "/gioco/guide",
            "credits": "/gioco/credits"
        }
    })

@gioco_blueprint.route("/gioco/about", methods=["GET"])
def about():
    return jsonify({
        "title": "Chi siamo",
        "content": "Testo about..."
    })

@gioco_blueprint.route("/gioco/guide", methods=["GET"])
def guide():
    return jsonify({
        "title": "Guida al gioco",
        "content": "Testo guida..."
    })

@gioco_blueprint.route("/gioco/credits", methods=["GET"])
def credits():
    return jsonify({
        "title": "Credits",
        "content": "Ringraziamenti..."
    })
