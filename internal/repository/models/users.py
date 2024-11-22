from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
Base.__allow_unmapped__ = True


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
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


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='admin')


class Farmer(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    # Relationships
    user = relationship('User', back_populates='farmer')
    product = relationship('Product', back_populates='farmer', uselist=False)
    farm = relationship('Farm', back_populates='farmer', uselist=False)


class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    delivery_address = Column(String, nullable=False)
    # preferred_payment_id = Column(Integer, nullable=False)
    preferred_payment_id = Column(Integer, ForeignKey('payment_types.id'), nullable=False)

    user = relationship('User', back_populates='buyer')
    payment_type = relationship('PaymentType', back_populates='buyer')
