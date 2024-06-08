"""
This module defines the Patient model for the database.
"""

from ..database import Base
from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer)
    gender = Column(String(10))
    #notes = relationship("Note", back_populates="patient")