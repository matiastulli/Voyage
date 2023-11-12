import jwt
from flask import request, g
from flask_jwt_extended import decode_token
from app.controllers.database_controller import database_controller
from app.schemas.user import User

def authenticate_request():
    token = request.headers.get('Authorization')

    if token and token.startswith('Bearer '):
        token = token.replace('Bearer ', '')

        try:
            decoded_token = decode_token(token)
            mail = decoded_token['mail']

            # Aquí podrías cargar el usuario desde la base de datos utilizando mail
            session = database_controller.new_session()
            user = session.query(User).filter_by(mail=mail).first()
            session.close()

            if user:
                g.current_user = user
            else:
                g.current_user = None

        except jwt.ExpiredSignatureError:
            # Handle token expiration here
            g.current_user = None
        except jwt.InvalidTokenError:
            # Handle invalid token here
            g.current_user = None
    else:
        g.current_user = None
