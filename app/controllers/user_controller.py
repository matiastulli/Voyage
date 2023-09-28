from flask import request
from app.schemas.auth import *
from app.libs.database import database

class UserController:
    @staticmethod
    
    def create_user():
        data = request.json

        obj_user = User(
            name=data['name'],
            last_name=data['last_name'],
            mail=data['mail']
        )

        session = database.new_session()
        session.add(obj_user)
        session.commit()
        session.refresh(obj_user)

        return obj_user


user_controller = UserController()