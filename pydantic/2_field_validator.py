from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @field_validator("name")
    @classmethod
    def name_uppercase(cls, value):
        return value.upper()
    
    @field_validator("age",mode = "before")
    @classmethod
    def age_validation(cls,value):
        if value < 0  and value>120:
            raise ValueError("Age should be greater than 0 and less then 120")
        
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        domain_name = ["hdfc.com","icici.com"]

        valid_domain = value.split("@")[-1]
        if valid_domain not in domain_name:
            raise ValueError("Email domain name is not valid")
        
        return value