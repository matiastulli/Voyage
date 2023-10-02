from flask import Blueprint, jsonify
from app.controllers.authentication_controller import authentication_controller

authentication_bp = Blueprint('authentication', __name__)


@authentication_bp.route('/register', methods=['POST'])
def register():
    access_token = authentication_controller.register_user()
    
    if access_token:
        return jsonify(access_token=access_token)
    
    return jsonify(message='No se ha podido generar su usuario'), 401


@authentication_bp.route('/login', methods=['POST'])
def login():
    access_token = authentication_controller.login_user()

    if access_token:
        return jsonify(access_token=access_token)
    
    return jsonify(message='Credenciales incorrectas'), 401
