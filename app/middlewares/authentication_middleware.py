from loguru import logger
from flask import request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.controllers.database_controller import database_controller
from app.schemas.user import User, Role
import jwt

def authenticate_request():
    token = request.headers.get('Authorization')

    if token and token.startswith('Bearer '):
        try:
            verify_jwt_in_request()
            user_id = get_jwt_identity()

            with database_controller.DatabaseSession(database_controller) as session:
                user = session.query(User).join(Role).filter(User.id == user_id).first()
                
                if user:
                    g.current_user = {
                        "id": user.id,
                        "name": user.name,
                        "last_name": user.last_name,
                        "mail": user.mail,
                        "id_role": user.id_role,
                        "role_description": user.role.description
                    }
                else:
                    g.current_user = None

        except jwt.ExpiredSignatureError as exception:
            logger.error(f"Token expired: {exception}")
            g.current_user = None
        except jwt.InvalidTokenError as exception:
            logger.error(f"Invalid token: {exception}")
            g.current_user = None
    else:
        logger.error("No token provided")
        g.current_user = None
