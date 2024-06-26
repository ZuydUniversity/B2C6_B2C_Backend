'''
This module contains the Note model for the database.
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class Note(Base):
    '''
    The Note model for the database.
    '''
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))

specialists = relationship("Specialist", back_populates="note")

patients = relationship("Patient", back_populates="note")

sessions = relationship("Session", back_populates="note")
