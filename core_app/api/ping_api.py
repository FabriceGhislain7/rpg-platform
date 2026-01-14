from flask import Blueprint, jsonify

ping_blueprint = Blueprint("ping_api", __name__)

@ping_blueprint.route("/ping_url", methods=["GET"])
def ping_endpoint():
    """
    Health-check endpoint.
    Used to verify that the API server is running.
    """
    return jsonify({
        "status": "ok",
        "message": "RPG Platform is running"
    })