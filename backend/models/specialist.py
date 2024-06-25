'''
This module contains the Specialist model for the database.
'''
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from backend.models.user import User

class Specialist(User):
    '''
    This is a child class of user.
    '''
    __tablename__ = "specialists"

specialist_patient_association = Table('patient_specialist_association', User.metadata,
    Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    Column('specialist_id', Integer, ForeignKey('specialists.id'), primary_key=True)
)
patients = relationship("Patient", secondary=specialist_patient_association, back_populates="specialists")

notes = relationship("Note", back_populates="specialist")

sessions = relationship("Session", back_populates="specialist")

appointments = relationship("Appointment", back_populates="specialist")
