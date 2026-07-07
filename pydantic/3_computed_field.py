from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi =  round(self.weight/(self.height**2),2)
        return bmi
    
patient_data = patient_data = {
    "name": "Ananya Sharma",
    "email": "ananya.sharma@example.com",
    "age": 29,
    "weight": 90.0,
    "height": 1.65,
    "married": False,
    "allergies": [
        "Dust",
        "Peanuts"
    ],
    "contact_details": {
        "phone": "9876543210",
        "emergency": "9876500001"
    }
}

patient1 = Patient(**patient_data)

def update_patient_data(patient:Patient):
    print(f"Patient Name:{patient.name}, Email:{patient.email}, Allegies:{patient.allergies}, contact details:{patient.contact_details}, BMI:{patient.bmi}", sep = "\n")

update_patient_data(patient1)