from sqlalchemy.ext.declarative import declarative_base # This should go in database.py once its made.
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship 

Base = declarative_base() # This should go in database.py once its made.

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    firstName = Column(String(50))  
    lastName = Column(String(50)) 
    email = Column(String(100))  
    age = Column(Integer)
    phonenumber = Column(Integer)  
    gender = Column(String(10))  
    contactpersonEmail = Column(String(100))  
    contactpersonPhonenumber = Column(Integer)


    # '''
    # The relationships will be defined here. Models yet to be added so the relationships are commented out.
    # '''
    # patient_specialist_association = Table('patient_specialist_association', Base.metadata,
    #     Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    #     Column('specialist_id', Integer, ForeignKey('specialists.id'), primary_key=True)
    # )
    # specialists = relationship("Specialist", secondary=patient_specialist_association, back_populates="patients")

    # notes = relationship("Note", backref="patient")

    # patient_medication_association = Table('patient_medication_association', Base.metadata,
    #     Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True),
    #     Column('medication_id', Integer, ForeignKey('medication.id'), primary_key=True)
    # )
    # medication = relationship("Medication", secondary=patient_medication_association, back_populates="patients")   

    # appointments = relationship("Appointment", backref="patient")


