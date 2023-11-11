from flask import Blueprint
from app.controllers.role_controller import role_controller

role_bp = Blueprint('role', __name__)

@role_bp.route('/create', methods=['POST'])
def create_role():
    result = role_controller.create_role()
    return result

@role_bp.route('/<int:role_id>', methods=['GET'])
def get_role(role_id):
    result = role_controller.get_role(role_id)
    return result

@role_bp.route('/update/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    result = role_controller.update_role(role_id)
    return result

@role_bp.route('/delete/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    result = role_controller.delete_role(role_id)
    return result
