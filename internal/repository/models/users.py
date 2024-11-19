from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
Base.__allow_unmapped__ = True  # Enable allow_unmapped for all models


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    approved = Column(Integer, nullable=False, default=0)
    active = Column(Integer, nullable=False, default=1)

    admin = relationship('Admin', back_populates='user', uselist=False)
    farmer = relationship('Farmer', back_populates='user', uselist=False)
    buyer = relationship('Buyer', back_populates='user', uselist=False)

    role: str

    # Relationship to Image
    images = relationship('Image', back_populates='user')


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='admin')


class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='farmer')


class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    delivery_address = Column(String, nullable=False)
    preferred_payment_id = Column(Integer, nullable=False)
    # preferred_payment_id = Column(Integer, ForeignKey('payment_types.id'), nullable=False)

    user = relationship('User', back_populates='buyer')


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to User
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='images')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Example relationship (optional, depending on requirements)
    image_id = Column(Integer, ForeignKey('images.id'), nullable=True)
    image = relationship('Image')
