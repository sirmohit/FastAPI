from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Literal,Optional,Annotated
import json

app = FastAPI()

def load_data():
    with open("patient.json","r") as f:
        data = json.load(f)
    return data

# creating a route for the root endpont
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully fuctional API to manage your patients recors"}

# endpoint of the API to view all the patients records
@app.get("/view")
def view():
    data = load_data()
    return data

# endpoint of the API to view a specific patient record by ID
@app.get("/patient/{patient_id}")
def get_patient(patient_id:str = Path(..., description = "The ID of the patient in the database", example="P001")):
    # load the data of al the patients
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    # If the patient data is not fount raise the HTTPException with status code 404
    raise HTTPException(status_code = 404, detail = f"Patient with id {patient_id} not found")

# endpoint of the API to demo Query Parameters
@app.get("/sort")
def sort_patients(sort_by:str = Query(..., description = 'Sort on the basis of the height,weight or bmi')
                  , order:str = Query('asc', description = 'sort in the ascending or descending order')):
    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f"Invalid field select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = "Invalid order select between 'asc' or 'desc'")
    
    data = load_data()

    sorted_data = sorted(data.values(), key = lambda x:x[sort_by], reverse = True if order == 'desc' else False)

    return sorted_data
    
#------------------------------------------------

# creating a route to add a new patient record to the database

class Patient(BaseModel):
    id: Annotated[str, Field(...,description = "The ID of the patient", examples = ["P001"])]
    name: Annotated[str, Field(..., description = "The name of the patient")]
    email: Annotated[EmailStr, Field(..., description = "The emial of the patient")]
    city: Annotated[str, Field(..., description = "The city of the patient")]
    age: Annotated[int, Field(...,gt = 0,lt =120, description = "The age of the patient")]
    gender: Annotated[Literal["Male","Female","Other"],Field(..., description = "Gender of the aptient")]
    height:float
    weight: float
    married: bool
    allergies:List[str]
    contact_details: Dict[str,str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18:
            return "Underweight"
        elif self.bmi > 18:
            return "Normal"
        elif self.bmi > 25:
            return "Overweight"
        else:
            return "Obese"
        
# save the new data into json format 
def save_data(data):
    with open("patient.json","w") as f:
        json.dump(data,f)

    
    
        
@app.post("/create")
def create_patient(patient:Patient):

    # load the existing data of all the patients
    data = load_data()

    # valide the patient id if it already exists in the database we will raise an HttpException with status code 400
    if patient.id in data:
        raise HTTPException(status_code = 400,detail = "Patient already exsits")
    
    #new patient add to database
    data[patient.id] = patient.model_dump(exclude = {"id"})

    # save data into file
    save_data(data)

    return JSONResponse(status_code = 201,content = {"message":"Patient created successfully"})
                  