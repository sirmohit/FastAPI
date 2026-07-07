# Expoting the pydantic model to json file or dictonary file and then importing it to another file and using it in the model_validator.py file

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
#print(patient1)
#print(patient1.address.city,patient1.address.state,patient1.address.pin,sep = "\n")

patient_dict = patient1.model_dump(include = {"name","gender"})
patient_json = patient1.model_dump_json(exclude = {"address":{"pin"}})

print(patient_dict)
print(type(patient_dict))

print(patient_json)
print(type(patient_json))


'''
# Exporting the model to a JSON file
with open("patient_data.json", "w") as f:
    json.dump(patient1.dict(), f)

# Importing the model from a JSON file
with open("patient_data.json", "r") as f:
    patient_data = json.load(f)

# Using the imported data to create a new instance of the model
patient2 = Patient(**patient_data)'''

