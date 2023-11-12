from flask import Blueprint
from app.controllers.event_controller import event_controller

event_bp = Blueprint('event', __name__)

@event_bp.route('/create', methods=['POST'])
def create():
    result = event_controller.create_event()
    return result

@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    result = event_controller.get_event(event_id)
    return result
