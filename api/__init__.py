from flask import Blueprint
from api.v1.routes import v1

# Crea un blueprint di base per l'API
api = Blueprint('api', __name__)

# Registra le versioni dell'API
api.register_blueprint(v1, url_prefix='/v1')