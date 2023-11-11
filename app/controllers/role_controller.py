import json
from flask import request
from app.schemas.user import Role
from app.controllers.database_controller import database_controller


class RoleController:

    def create_role(self) -> str:
        data = request.json
        with database_controller.DatabaseSession(database_controller) as session:
            new_role = Role(description=data['description'])
            session.add(new_role)
            session.flush()
            role_id = new_role.id

        return json.dumps({'message': 'Role created', 'id': role_id})

    def get_role(self, role_id: int) -> str:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                role_data = {'message': 'Role not found'}
                return json.dumps(role_data)
            
            role_data = {'id': role.id, 'description': role.description}    
        
        return json.dumps(role_data)

    def update_role(self, role_id: int) -> str:
        data = request.json
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                role_data = {'message': 'Role not found'}
                return json.dumps(role_data)
            
            role.description = data.get('description', role.description)
            
        return json.dumps({'message': 'Role updated'})

    def delete_role(self, role_id: int) -> str:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                role_data = {'message': 'Role not found'}
                return json.dumps(role_data)
        
            session.delete(role)
        
        return json.dumps({'message': 'Role deleted'})

role_controller = RoleController()
