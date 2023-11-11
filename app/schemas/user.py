from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.base_utils import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'user'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    mail = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    id_role = Column(Integer, ForeignKey('user.role.id'))
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    role = relationship('Role')

    def set_password(self, password):
        # Genera un hash seguro a partir de la contraseña proporcionada
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verifica si la contraseña proporcionada coincide con el hash almacenado
        return check_password_hash(self.password_hash, password)


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'schema': 'user'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(50), nullable=False)


class UserActivityLog(Base):
    __tablename__ = 'user_activity_log'
    __table_args__ = {'schema': 'user'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.user.id'))
    action = Column(String(100), nullable=False)
    datetime = Column(DateTime, nullable=False)
    
    user = relationship('User')


class UserPayment(Base):
    __tablename__ = 'user_payment'
    __table_args__ = {'schema': 'user'}

    id_user = Column(Integer, ForeignKey('user.user.id'), primary_key=True)
    id_payment_method = Column(Integer, ForeignKey('user.payment_method.id'), primary_key=True)
    priority = Column(Integer)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    user = relationship('User')
    payment_method = relationship('PaymentMethod')


class PaymentMethod(Base):
    __tablename__ = 'payment_method'
    __table_args__ = {'schema': 'user'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    method_type = Column(String(100), nullable=False)


class Notification(Base):
    __tablename__ = 'notification'
    __table_args__ = {'schema': 'user'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.user.id'))
    message = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    read_at = Column(DateTime, nullable=True)
    
    user = relationship('User')
