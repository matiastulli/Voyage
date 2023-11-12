import os
import jwt
from loguru import logger
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from app.controllers.database_controller import database_controller
from app.schemas.user import User, Role

class AuthenticateRequest(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        token = request.headers.get("Authorization")

        if token and token.startswith('Bearer '):

            token = token.replace("Bearer ", "")
            user = await self.authenticate_token(token)
            if not user:
                raise Exception("Unauthorized") #type: ignore
            
            request.state.user = user
        else:
            logger.info("No token provided")
            request.state.user = None
        
        return await call_next(request)


    async def authenticate_token(self, token: str):
        try:
            decoded_token = jwt.decode(token, os.environ.get("ENV_JWT_SECRET_KEY"), algorithms=["HS256"]) #type: ignore
            with database_controller.DatabaseSession(database_controller) as session:
                user = session.query(User).join(Role).filter(User.id == decoded_token["id"]).first()
                if not user:
                    return None
                
                user = {
                    "id": user.id,
                    "name": user.name,
                    "last_name": user.last_name,
                    "mail": user.mail,
                    "id_role": user.id_role,
                    "role_description": user.role.description
                }
                return user

        except jwt.ExpiredSignatureError as exception:
            logger.error(f"Token expired: {exception}")
            raise Exception("Token expired") from exception #type: ignore
        except jwt.InvalidTokenError as exception:
            logger.error(f"Invalid token: {exception}")
            raise Exception("Invalid token") from exception #type: ignore
