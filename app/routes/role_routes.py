from fastapi import APIRouter, Request
from app.models.role_model import RoleCreate, RoleUpdate
from app.controllers.role_controller import role_controller
from app.decorators.role_required_decorator import requires_role

router = APIRouter()

@router.post('/create')
@requires_role("admin")
async def create_role(request: Request, role: RoleCreate):
    result = await role_controller.create_role(role)
    return result

@router.get('/{role_id}')
@requires_role("admin")
async def get_role(request: Request, role_id: int):
    result = await role_controller.get_role(role_id)
    return result

@router.put('/update')
@requires_role("admin")
async def update_role(request: Request, role: RoleUpdate):
    result = await role_controller.update_role(role)
    return result

@router.delete('/delete/{role_id}')
@requires_role("admin")
async def delete_role(request: Request, role_id: int):
    result = await role_controller.delete_role(role_id)
    return result
