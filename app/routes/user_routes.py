from flask import Blueprint
from app.controllers.user_controller import user_controller

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    result = user_controller.register_user()
    return result

@user_bp.route('/login', methods=['POST'])
def login_user():
    result = user_controller.login_user()
    return result
