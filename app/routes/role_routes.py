from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.role_controller import role_controller
from app.decorators.role_required_decorator import requires_role

role_bp = Blueprint('role', __name__)

@role_bp.route('/create', methods=['POST'])
@jwt_required()
@requires_role('administrador')
def create_role():
    result = role_controller.create_role()
    return result

@role_bp.route('/<int:role_id>', methods=['GET'])
@jwt_required()
@requires_role('administrador')
def get_role(role_id):
    result = role_controller.get_role(role_id)
    return result

@role_bp.route('/update/<int:role_id>', methods=['PUT'])
@jwt_required()
@requires_role('administrador')
def update_role(role_id):
    result = role_controller.update_role(role_id)
    return result

@role_bp.route('/delete/<int:role_id>', methods=['DELETE'])
@jwt_required()
@requires_role('administrador')
def delete_role(role_id):
    result = role_controller.delete_role(role_id)
    return result
