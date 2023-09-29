from flask import Flask, request
from flask_jwt_extended import JWTManager
from app.middlewares.logger_middleware import create_auth_middleware
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    jwt = JWTManager(app)

    app.register_blueprint(user_bp, url_prefix='/user')

    auth_middleware = create_auth_middleware(app)
    app.before_request(auth_middleware)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
