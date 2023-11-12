from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.utils.base_utils import Base

class Event(Base):
    __tablename__ = 'event'
    __table_args__ = {'schema': 'event'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    status = Column(String(50), nullable=True)
    id_user = Column(Integer, ForeignKey('user.user.id'))
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    user = relationship('User')
    
    
class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(50), nullable=False)


class EventCategory(Base):
    __tablename__ = 'event_category'
    __table_args__ = {'schema': 'event'}
    
    id_event = Column(Integer, ForeignKey('event.event.id'), primary_key=True)
    id_category = Column(Integer, ForeignKey('event.category.id'), primary_key=True)

    event = relationship('Event')
    category = relationship('Category')


class Image(Base):
    __tablename__ = 'image'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(255), nullable=False)
    description = Column(String(100), nullable=False)
    file_size = Column(Float)
    format = Column(String(50))
    dimensions = Column(String(50))
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    

class EventImage(Base):
    __tablename__ = 'event_image'
    __table_args__ = {'schema': 'event'}
    
    id_event = Column(Integer, ForeignKey('event.event.id'), primary_key=True)
    id_image = Column(Integer, ForeignKey('event.image.id'), primary_key=True)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    event = relationship('Event')
    image = relationship('Image')


class Location(Base):
    __tablename__ = 'location'
    __table_args__ = {'schema': 'event'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    type = Column(String(20), nullable=False)
    parent_id_location = Column(Integer, ForeignKey('event.location.id'), nullable=True)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    location = relationship('Location')

    
class EventLocation(Base):
    __tablename__ = 'event_location'
    __table_args__ = {'schema': 'event'}
    
    id_event = Column(Integer, ForeignKey('event.event.id'), primary_key=True)
    id_location = Column(Integer, ForeignKey('event.location.id'), primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    event = relationship('Event')
    location = relationship('Location')


class Review(Base):
    __tablename__ = 'review'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_subscription = Column(Integer, ForeignKey('event.subscription_event.id'))
    review_text = Column(String(100), nullable=False)
    rating = Column(Integer)
    date_reviewed = Column(DateTime)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    subscription = relationship('SubscriptionEvent')


class SubscriptionEvent(Base):
    __tablename__ = 'subscription_event'
    __table_args__ = {'schema': 'event'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.user.id'))
    id_event = Column(Integer, ForeignKey('event.event.id'))
    subscription_status = Column(String(20), nullable=False)
    date_subscribed = Column(DateTime)
    date_unsubscribed = Column(DateTime)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    deleted_at = Column(DateTime)

    user = relationship('User')
    event = relationship('Event')


class Service(Base):
    __tablename__ = 'service'
    __table_args__ = {'schema': 'event'}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())


class EventService(Base):
    __tablename__ = 'event_service'
    __table_args__ = {'schema': 'event'}

    id_event = Column(Integer, ForeignKey('event.event.id'), primary_key=True)
    id_service = Column(Integer, ForeignKey('event.service.id'), primary_key=True)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    event = relationship('Event')
    service = relationship('Service')
