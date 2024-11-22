from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from internal.repository.models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    # Relationships
    product = relationship('Product', back_populates='category', uselist=False)
