from pydantic import BaseModel, EmailStr,AnyUrl,Field,HTTPException,Query,computed_field
from typing import List,Dict,Optional,Annotated
import json

class Patient(BaseModel):
    name:Annotated[str, Field(..., max_length = 50, title = "Name of the patient", description  = "Give the name of the patient")]
    email:EmailStr # this field will be validated as an email address a data type of EmailStr is used from pydantic
    linkedIn:AnyUrl # this field will be validated as a url a data type of AnyUrl is used from pydantic
    age:int = Field(...,gt = 0,lt = 120, description = "Age of the patient should be greater then 0 and less then 120") # this field will be validated to be greater than 0 and less than 120 using Field from pydantic)
    weight:Annotated[float,Field(...,gt = 0, strict = True,description = "Weight of the patient should be greater then 0")]
    married:Optional[bool] = False # this field is optional and if not provided it will be set to False
    allergies:List[str]  = Field(max_items = 5, description = "the list of the allergies should not contain more than 5 items") # this field is a list of strings and it will be validated to have a maximum of 5 items)
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name,patient.email,end = "\n")
    print(patient.age,end = "\n")
    print(patient.weight,end = "\n")
    print(patient.married,patient.allergies,patient.contact_details,sep = "\n")
    print("insert")

patient_data = {"name":"John", "email":"john@gmail.com", "linkedIn":"http://www.linkedin.com/in/john", "age":40,"weight":70,"married":True,"allergies":["pollen","dust"],"contact_details":{"email":"joe@gmail.com","phone":"6738774843"}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)
