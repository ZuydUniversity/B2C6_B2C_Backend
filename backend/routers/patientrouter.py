from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..common import get_db
from ..models import Patient
from ..schemas import PatientCreate, PatientResponse

router = APIRouter()

@router.post("/patients/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return PatientResponse.from_orm(db_patient)

@router.get("/patients/{patient_id}", response_model=PatientResponse)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Patient).filter(Patient.Id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return PatientResponse.from_orm(db_patient)
