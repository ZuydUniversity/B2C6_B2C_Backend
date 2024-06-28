'''
This module contains the Note model for the database.
'''
from sqlalchemy import Column, Integer, String, ForeignKey
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

    specialist_id = Column(Integer, ForeignKey('specialists.id'))
    specialist = relationship("Specialist", back_populates="notes")

    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship("Patient", back_populates="notes")

    session_id = Column(Integer, ForeignKey('sessions.id'))
    session = relationship("Session", back_populates="notes")