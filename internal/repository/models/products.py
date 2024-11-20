from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.__allow_unmapped__ = True


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    farmer_id = Column(Integer, ForeignKey('farmers.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    weight = Column(Numeric(5, 2), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
