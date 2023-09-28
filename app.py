from flask import Flask
from flask_jwt_extended import JWTManager
from app.routes.auth_routes import auth_bp

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Registra el blueprint de autenticación
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run()