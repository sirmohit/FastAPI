import json

from pydantic import BaseModel,EmailStr,AnyUrl,model_validator

from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode = "before")
    @classmethod
    def validate_emergency_contact(cls,model):
        if  model.get("age", 0) > 60 and model.get("emergency") not in model.get("contact_details", {}):
            raise ValueError("Emergency contact is required for patient")
        return model
    
def update_patient_data(patient:Patient):
    print(f"Patient Name:{patient.name}, Email:{patient.email}, Allegies:{patient.allergies}, contact details:{patient.contact_details}", sep = "\n")

def get_data():
    with open("patient.json","r") as f:
        data = json.load(f)
    return data

patient_data = Patient(**get_data()["P001"])

update_patient_data(patient_data)