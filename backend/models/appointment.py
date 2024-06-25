from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from backend.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_keys=True)
    title = Column(String(50))
    description = Column(String(100))
    periodical = Column(String(50))
    starttime = Column(String(50))
    endtime = Column(String(50))

# Relationships
appointment_patient_association = Table('appointment_patient_association', Base.metadata, 
    Column('appointment_id', Integer, ForeignKey('appointments.id'), primary_key=True), 
    Column('patient_id', Integer, ForeignKey('patients.id'), primary_key=True)
)

patients = relationship("Patient", secondary=appointment_patient_association, back_populates="appointments")


