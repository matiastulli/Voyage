from flask import Blueprint, jsonify
from app.controllers.user_controller import user_controller

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile', methods=['GET'])
def profile():
    user = user_controller.profile()
    
    return jsonify(user), 401