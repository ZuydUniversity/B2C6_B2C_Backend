from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    session_id = Column(Integer)
    patient_id = Column(Integer)
    specialist_id = Column(Integer)