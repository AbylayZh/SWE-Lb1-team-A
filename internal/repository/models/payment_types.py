from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from internal.repository.models.base import Base


class PaymentType(Base):
    __tablename__ = 'payment_types'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    # Relationships
    buyer = relationship('Buyer', back_populates='payment_type', uselist=False)
