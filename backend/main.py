from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Patient

app = FastAPI()

origins = ["*"] # allow any connection for now

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/patients/")
async def create_patient(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    print(f"Received a request: {data}")
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    patient = Patient(name=name, age=age, gender=gender)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@app.get("/patients/")
async def read_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients

Base.metadata.create_all(bind=engine)


# # hardcoded to see if connection works
# if __name__ == "__main__": # (run main.py directly to make this work)
#     db = SessionLocal()
#     patient = Patient(name="John Doe", age=30, gender="Male")
#     db.add(patient)
#     db.commit()
#     db.close()