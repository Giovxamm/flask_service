from flask import Blueprint, request, jsonify

# Crea un blueprint per l'API v1
v1 = Blueprint('v1', __name__)

@v1.route("/greet", methods=["GET"])
def greet():
    # Ottieni il parametro 'name' dalla query string
    name = request.args.get("name", "World")
    # Risposta
    response = {
        "message": f"Hello {name}!"
    }
    return jsonify(response), 200