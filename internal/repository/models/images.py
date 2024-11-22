from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from internal.repository.models.base import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # product_id = Column(Integer, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    path = Column(String, nullable=True)
    created = Column(DateTime, default=datetime.utcnow)

    product = relationship('Product', back_populates='image')
