from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_data = {"city":"Pue","state":"MH","pin":"123452"}
address1 = Address(**address_data)

patient_data = {"name":"Ananya Sharma","gender":"Female","age":43,"address":address1}
patient1 = Patient(**patient_data)
print(patient1)
print(patient1.address.city,patient1.address.state,patient1.address.pin,sep = "\n")
