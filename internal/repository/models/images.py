from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.__allow_unmapped__ = True


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    # product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    path = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
