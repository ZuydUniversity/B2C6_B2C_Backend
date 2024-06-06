'''
Contains models that store data
'''
from pydantic import BaseModel
from ..Models import sessionmodel, patientmodel, specialistmodel

class Note(BaseModel):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    Id: int
    Name: str
    Session: sessionmodel.Session
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
