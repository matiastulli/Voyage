from typing import Tuple
from flask import request, Response, jsonify
from flask_jwt_extended import create_access_token
from app.schemas.user import User
from app.controllers.database_controller import database_controller

class UserController:
    
    def register_user(self) -> Tuple[Response, int]:
        data = request.json
        
        new_user = User(
            name=data['name'],
            last_name=data['last_name'],
            mail=data['mail'],
            id_role=data['id_role']
        )
        
        new_user.set_password(data['password'])
        
        with database_controller.DatabaseSession(database_controller) as session:
            session.add(new_user)
            session.flush()
            user_id = new_user.id
            
            claims = {
                "name": new_user.name,
                "last_name": new_user.last_name,
                "mail": new_user.mail,
                "id_role": new_user.id_role
            }

        access_token = create_access_token(identity=user_id, additional_claims=claims)
        
        if not access_token:
            return jsonify({'error': 'No se ha podido generar su usuario'}), 400
        
        return jsonify({'message': 'User created', 'id': user_id, 'access_token': access_token}), 200
    
    
    def login_user(self) -> Tuple[Response, int]:
        data = request.json
        
        with database_controller.DatabaseSession(database_controller) as session:
            user = session.query(User).filter_by(mail=data['mail']).first()
            
        if user and user.check_password(data['password']):
            claims = {"name": user.name,
                    "last_name": user.last_name,
                    "mail": user.mail}
            access_token = create_access_token(identity=user.id, 
                                               additional_claims= claims)
            return jsonify({'message': 'User loged', 'access_token': access_token}), 200
        
        return jsonify({'Credenciales incorrectas'}), 400

user_controller = UserController()