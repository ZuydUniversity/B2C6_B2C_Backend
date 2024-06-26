'''
This module contains the Mediaction model for the database.
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from backend.database import Base

class Medication(Base):
    '''
    Pylint nono.
    '''
    __tablename__ = "medication"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

medication_patient_association = Table('medication_patient_association', Base.metadata,
    Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    Column('medication_id', Integer, ForeignKey('medication.id'), primary_key=True)
)
patients = relationship("Patient", secondary=medication_patient_association, back_populates="medication")
