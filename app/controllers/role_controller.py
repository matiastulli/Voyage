from typing import Tuple
from flask import request, Response, jsonify
from app.schemas.user import Role
from app.controllers.database_controller import database_controller


class RoleController:

    def create_role(self) -> Tuple[Response, int]:
        data = request.json
        with database_controller.DatabaseSession(database_controller) as session:
            new_role = Role(description=data['description'])
            session.add(new_role)
            session.flush()
            role_id = new_role.id

        return jsonify({'message': 'Role created', 'id': role_id}), 200

    def get_role(self, role_id: int) -> Tuple[Response, int]:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                return jsonify({'message': 'Role not found'}), 404
            
            role = {
                "id": role.id,
                "description": role.description
            }
            
            return jsonify({'role': role}), 200

    def update_role(self, role_id: int) -> Tuple[Response, int]:
        data = request.json
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                return jsonify({'message': 'Role not found'}), 404
            
            role.description = data.get('description', role.description)
            
        return jsonify({'message': 'Role updated'}), 200

    def delete_role(self, role_id: int) -> Tuple[Response, int]:
        with database_controller.DatabaseSession(database_controller) as session:
            role = session.query(Role).get(role_id)
            if not role:
                return jsonify({'message': 'Role not found'}), 404
        
            session.delete(role)
        
        return jsonify({'message': 'Role deleted'}), 200

role_controller = RoleController()
