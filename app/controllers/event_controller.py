from typing import Tuple
from flask import request, Response, jsonify
from app.schemas.event import Event
from app.controllers.database_controller import database_controller


class EventController:

    def create_event(self) -> Tuple[Response, int]:
        data = request.json
        with database_controller.DatabaseSession(database_controller) as session:
            new_event = Event(**data)
            session.add(new_event)
            session.flush()
            event_id = new_event.id
            
        return jsonify({'message': 'New event created', 'id': event_id}), 200

    def get_event(self, event_id: int) -> Tuple[Response, int]:
        with database_controller.DatabaseSession(database_controller) as session:
            event = session.query(Event).get(event_id)
            if not event:
                return jsonify({'message': 'Event not found'}), 404
            
            event = {
                "id": event.id,
                "description": event.description,
                "status": event.status,
                "id_user": event.id_user,
                "created_at": event.created_at.strftime("%Y-%m-%dT%H:%M:%S") if event.created_at else None,
                "updated_at": event.updated_at.strftime("%Y-%m-%dT%H:%M:%S") if event.updated_at else None
            }
            
            return jsonify({'event': event}), 200

event_controller = EventController()
