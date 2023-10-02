from flask import request
from app.schemas.auth import User
from app.controllers.database_controller import database_controller

class UserController:
    
    def profile(self):
        data = request.json
        
        session = database_controller.new_session()
        user = session.query(User).filter_by(mail=data['mail']).first()
        session.close()
        
        return user


user_controller = UserController()