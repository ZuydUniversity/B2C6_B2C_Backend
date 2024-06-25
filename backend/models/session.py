'''
This module contains the Session model for the database.
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship
from backend.database import Base

class Session(Base):
    '''
    Pylint nono
    '''
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    name = Column(String(50))

specialists = relationship("Specialist", back_populates="sessions")

patient = relationship("Patient", back_populates="sessions")

appointments = relationship("Appointment", back_populates="session")

notes = relationship("Note", back_populates="session")