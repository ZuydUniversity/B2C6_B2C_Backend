from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    session_id: int
    patient_id: int
    specialist_id: int

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True