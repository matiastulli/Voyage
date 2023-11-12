from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.event_controller import event_controller
from app.decorators.role_required_decorator import requires_role

event_bp = Blueprint('event', __name__)

@event_bp.route('/create', methods=['POST'])
@jwt_required()
@requires_role('administrador')
def create():
    result = event_controller.create_event()
    return result

@event_bp.route('/<int:event_id>', methods=['GET'])
@jwt_required()
@requires_role('administrador')
def get_event(event_id):
    result = event_controller.get_event(event_id)
    return result
