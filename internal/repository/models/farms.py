from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Farm(Base):
    __tablename__ = 'farms'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    farmer_id = Column(Integer, ForeignKey('farmers.id', ondelete="CASCADE"), nullable=False)
    size = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    # Define relationships
    farmer = relationship('Farmer', back_populates='farm')
