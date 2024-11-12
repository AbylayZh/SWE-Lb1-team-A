from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Farm(Base):

    __tablename__ = 'farms'

    # Define columns
    farmId = Column(Integer, primary_key=True, autoincrement=True)
    farmSize = Column(Integer, nullable=False)
    farmerId = Column(Integer, ForeignKey('farmers.id'), nullable=False)
    farmAddress = Column(String, nullable=False)

    # Define relationships
    produce = relationship("Produce", back_populates="farm")  # Assume a `Produce` model exists
    supervises = relationship("Supervisor", back_populates="farm")  # Assume a `Supervisor` model exists