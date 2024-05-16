from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
from models import Patient

app = FastAPI()

origins = [
    "http://localhost:3000",  # React's default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/patients/")
async def create_patient(request: Request):
    data = await request.json()
    print(f"Received a request: {data}")
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    db = SessionLocal()
    patient = Patient(name=name, age=age, gender=gender)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    db.close()
    return patient

@app.get("/patients/")
async def read_patients():
    db = SessionLocal()
    patients = db.query(Patient).all()
    db.close()
    return patients

Base.metadata.create_all(bind=engine)


# # hardcoded to see if connection works
# if __name__ == "__main__": # (run main.py directly to make this work)
#     db = SessionLocal()
#     patient = Patient(name="John Doe", age=30, gender="Male")
#     db.add(patient)
#     db.commit()
#     db.close()