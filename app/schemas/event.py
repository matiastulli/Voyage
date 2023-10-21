from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from app.utils.base_utils import Base
from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = 'event'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sdes = Column(String(255))
    date = Column(Date)
    

class Country(Base):
    __tablename__ = 'country'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sdes = Column(String(255))


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sdes = Column(String(255))
    

class EventLocation(Base):
    __tablename__ = 'event_location'
    __table_args__ = {'schema': 'event'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_event = Column(ForeignKey('event.event.id'))
    id_country = Column(ForeignKey('event.country.id'))
    id_city = Column(ForeignKey('event.city.id'))
    
    event = relationship('event')
    country = relationship('country')
    city = relationship('city')


class SubscriptionEvent(Base):
    __tablename__ = 'subscriptionEvent'
    __table_args__ = {'schema': 'event'}
    
    id_user = Column(Integer, ForeignKey('auth.user.id'), primary_key=True)
    id_event = Column(Integer, ForeignKey('event.event.id'), primary_key=True)
    
    user = relationship('user')
    event = relationship('event')

