'''
This module contains the Appointment model for the database.
'''
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from backend.database import Base

class Appointment(Base):
    '''
    Pylint nono
    '''
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    name = Column(String(50))

sessions = relationship("Session", back_populates="appointment")

specialists = relationship("Specialist", back_populates="appointment")

patients = relationship("Patient", back_populates="appointment")
