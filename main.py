import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from app.middlewares.authentication_middleware import authenticate_request
from app.middlewares.activity_logger_middleware import log_activity
from app.routes.user_routes import user_bp
from app.routes.role_routes import role_bp

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get("ENV_JWT_SECRET_KEY")
jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(role_bp, url_prefix='/role')

app.before_request(authenticate_request)
app.before_request(log_activity)

if __name__ == '__main__':
    app.run()