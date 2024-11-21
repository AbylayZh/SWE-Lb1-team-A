from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    # Relationships
    # products = relationship('Product', back_populates='category')
