from flask import request
from app.schemas.auth import User
from app.libs.database import database
from flask_jwt_extended import create_access_token

class UserController:
    
    def create_user(self):
        data = request.json

        user = User(
            name=data['name'],
            last_name=data['last_name'],
            mail=data['mail']
        )
        
        user.set_password(data['password'])

        session = database.new_session()
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
        
        session = database.new_session()
        user = session.query(User).filter_by(mail=data['mail']).first()

        if user and user.check_password(data['password']):
            claims = {"name": user.name,
                    "last_name": user.last_name,
                    "mail": user.mail}
            access_token = create_access_token(identity=user.id, 
                                               additional_claims= claims)
            return access_token

        return None


user_controller = UserController()