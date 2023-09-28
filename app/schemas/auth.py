from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.utils.base import Base

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    mail = Column(String(255), unique=True, nullable=False)
