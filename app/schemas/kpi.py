from sqlalchemy import Column, ForeignKey, Integer, JSON, DateTime, String
from sqlalchemy.orm import relationship
from app.utils.base_utils import Base

class Log(Base):
    __tablename__ = 'log'
    __table_args__ = {'schema': 'kpi'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_mail = Column(ForeignKey('user.user.mail'))
    body_data = Column(JSON)
    host = Column(String(255), nullable=False)
    route = Column(String(255), nullable=False)
    date = Column(DateTime(timezone=False))
    
    user = relationship('User')
