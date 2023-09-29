from flask import Blueprint, jsonify
from app.controllers.user_controller import user_controller

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    access_token = user_controller.create_user()
    
    if access_token:
        return jsonify(access_token=access_token)
    
    return jsonify(message='No se ha podido generar su usuario'), 401

@user_bp.route('/login', methods=['POST'])
def login():
    access_token = user_controller.login_user()

    if access_token:
        return jsonify(access_token=access_token)
    
    return jsonify(message='Credenciales incorrectas'), 401
