from sqlalchemy import Column, Integer, JSON, DateTime, String
from app.utils.base_utils import Base

class Log(Base):
    __tablename__ = 'log'
    __table_args__ = {'schema': 'kpi'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(255), nullable=False)
    body_data = Column(JSON)
    host = Column(String(255), nullable=False)
    route = Column(String(255), nullable=False)
    date = Column(DateTime(timezone=False))
