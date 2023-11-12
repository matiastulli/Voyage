from fastapi import APIRouter, Request
from app.models.event_model import EventCreate
from app.controllers.event_controller import event_controller
from app.decorators.role_required_decorator import requires_role

router = APIRouter()

@router.post('/create')
@requires_role("admin")
async def create(request: Request, event: EventCreate):
    result = await event_controller.create_event(event)
    return result

@router.get('/{event_id}')
async def get_event(request: Request, event_id: int):
    result = await event_controller.get_event(event_id)
    return result
