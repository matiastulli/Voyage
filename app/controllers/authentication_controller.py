from flask import request
from app.schemas.auth import User
from app.controllers.database_controller import database_controller
from flask_jwt_extended import create_access_token

class AuthenticationController:
    
    def register_user(self):
        data = request.json

        user = User(
            name=data['name'],
            last_name=data['last_name'],
            mail=data['mail']
        )
        
        user.set_password(data['password'])

        session = database_controller.new_session()
        session.add(user)
        session.commit()
        session.refresh(user)
        
        claims = {"name": user.name,
                  "last_name": user.last_name,
                  "mail": user.mail}
        access_token = create_access_token(identity=user.id, additional_claims= claims)

        return access_token
    
    
    def login_user(self):
        data = request.json
        
        session = database_controller.new_session()
        user = session.query(User).filter_by(mail=data['mail']).first()

        if user and user.check_password(data['password']):
            claims = {"name": user.name,
                    "last_name": user.last_name,
                    "mail": user.mail}
            access_token = create_access_token(identity=user.id, 
                                               additional_claims= claims)
            return access_token

        return None
        
authentication_controller = AuthenticationController()