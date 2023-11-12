from fastapi.responses import JSONResponse
from app.schemas.user import Role
from app.models.role_model import RoleCreate, RoleUpdate
from app.controllers.database_controller import database_controller


class RoleController:

    async def create_role(self, role: RoleCreate) -> JSONResponse:
        
        with database_controller.DatabaseSession(database_controller) as session:
            new_role = Role(**role.model_dump())
            session.add(new_role)
            session.flush()
            role_id = new_role.id

        return JSONResponse(content={'message': 'Role created', 'id': role_id}, status_code=200)

    async def get_role(self, role_id: int) -> JSONResponse:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                return JSONResponse(content={'message': 'Role not found'}, status_code=404)
            
            role = {
                "id": role.id,
                "description": role.description
            }
            
            return JSONResponse(content={'role': role}, status_code=200)

    async def update_role(self, role: RoleUpdate) -> JSONResponse:
        with database_controller.DatabaseSession(database_controller) as session:
            role_data = session.query(Role).get(role.id)
            if not role:
                return JSONResponse(content={'message': 'Role not found'}, status_code=404)
            
            role_data.description = role.description
            
        return JSONResponse(content={'message': 'Role updated'}, status_code=200)

    async def delete_role(self, role_id: int) -> JSONResponse:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                return JSONResponse(content={'message': 'Role not found'}, status_code=404)
        
            session.delete(role)
        
        return JSONResponse(content={'message': 'Role deleted'}, status_code=200)

role_controller = RoleController()
