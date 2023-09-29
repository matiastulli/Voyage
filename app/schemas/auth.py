from sqlalchemy import Column, Integer, String
from app.utils.base import Base
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    mail = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    
    def set_password(self, password):
        # Genera un hash seguro a partir de la contraseña proporcionada
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verifica si la contraseña proporcionada coincide con el hash almacenado
        return check_password_hash(self.password_hash, password)
