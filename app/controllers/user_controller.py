import os
from datetime import datetime, timedelta
from typing import Any
import jwt
from fastapi.responses import JSONResponse
from app.schemas.user import User
from app.models.user_model import UserCreate, UserRead
from app.controllers.database_controller import database_controller

class UserController:
    
    async def create_access_token(self, data: dict[str, Any], expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)  # Default expiry time
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.environ.get("ENV_JWT_SECRET_KEY"), algorithm="HS256")
        return encoded_jwt

    
    async def register_user(self, user: UserCreate) -> JSONResponse:
        
        new_user = User(
            name=user.name,
            last_name=user.last_name,
            mail=user.mail,
            id_role=user.id_role
        )
        
        new_user.set_password(user.password)
        
        with database_controller.DatabaseSession(database_controller) as session:
            session.add(new_user)
            session.flush()
            user_id = new_user.id
            
            claims = {
                "id": user_id,
                "name": new_user.name,
                "last_name": new_user.last_name,
                "mail": new_user.mail,
                "id_role": new_user.id_role
            }

        expires_duration = timedelta(days=30)
        access_token = await self.create_access_token(data=claims, expires_delta=expires_duration)
        
        if not access_token:
            return JSONResponse(content={'error': 'Error making acess token'}, status_code=400)
        
        return JSONResponse(content={'message': 'User created', 'id': user_id, 'access_token': access_token}, status_code=200)
    
    
    async def login_user(self, user: UserRead) -> JSONResponse:
        
        with database_controller.DatabaseSession(database_controller) as session:
            user_data = session.query(User).filter_by(mail=user.mail).first()
            session.flush()
            
            if not user_data and not user_data.check_password(user.password):
                return JSONResponse(content={'Invalid credentials'}, status_code=400)
            
            claims = {
                "id": user_data.id,
                "name": user_data.name,
                "last_name": user_data.last_name,
                "mail": user_data.mail
            }
            
        expires_duration = timedelta(days=30)
        access_token = await self.create_access_token(data=claims, expires_delta=expires_duration)
        return JSONResponse(content={'message': 'User loged', 'access_token': access_token}, status_code=200)
        

user_controller = UserController()