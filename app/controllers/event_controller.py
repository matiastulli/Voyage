from fastapi.responses import JSONResponse
from app.schemas.event import Event
from app.models.event_model import EventCreate
from app.controllers.database_controller import database_controller


class EventController:

    async def create_event(self, event: EventCreate) -> JSONResponse:
    
        with database_controller.DatabaseSession(database_controller) as session:
            new_event = Event(**event.model_dump())
            session.add(new_event)
            session.flush()
            event_id = new_event.id
            
        return JSONResponse(content={'message': 'New event created', 'id': event_id}, status_code=200)

    async def get_event(self, event_id: int) -> JSONResponse:
        with database_controller.DatabaseSession(database_controller) as session:
            event = session.query(Event).get(event_id)
            if not event:
                return JSONResponse(content={'message': 'Event not found'}, status_code=404)
            
            event = {
                "id": event.id,
                "description": event.description,
                "status": event.status,
                "id_user": event.id_user,
                "created_at": event.created_at.strftime("%Y-%m-%dT%H:%M:%S") if event.created_at else None,
                "updated_at": event.updated_at.strftime("%Y-%m-%dT%H:%M:%S") if event.updated_at else None
            }
            
            return JSONResponse(content={'event': event}, status_code=200)

event_controller = EventController()
