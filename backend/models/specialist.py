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

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'specialist',
        'inherit_condition': id == User.id
    }
    sessions = relationship("Session", back_populates="specialists")
    patients = relationship("Patient", secondary='patient_specialist_association', back_populates="specialists")
    notes = relationship("Note", back_populates="specialist")
    appointments = relationship("Appointment", back_populates="specialist")
    
specialist_patient_association = Table('patient_specialist_association', User.metadata,
    Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    Column('specialist_id', Integer, ForeignKey('specialists.id'), primary_key=True)
)
