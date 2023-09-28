from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token
from app.controllers.user_controller import user_controller

# Crea un Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    user = user_controller.create_user()
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@auth_bp.route('/login', methods=['POST'])
def login():
    user_id = 1  # ID del usuario autenticado
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token)
