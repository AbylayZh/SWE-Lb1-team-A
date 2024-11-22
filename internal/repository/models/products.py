from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
Base.__allow_unmapped__ = True


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    # farmer_id = Column(Integer, nullable=False)
    farmer_id = Column(Integer, ForeignKey('farmers.id', ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    # category_id = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    weight = Column(Numeric(5, 2), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    # Relationships
    farmer = relationship('Farmer', back_populates='product')
    category = relationship('Category', back_populates='product')
    image = relationship('image', back_populates='product', uselist=False)
