from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("models/regression_model.pkl")

# Input schema (exact 18 features in correct order)
class InputData(BaseModel):
    Length_ft: float
    Location: float
    Type: float
    Manufacturer: float
    Height_ft: float
    Duration_sec: float
    opening_date: float
    Inversions: float
    Launch_system_Elevator_lift: bool
    Launch_system_Hydraulic_Launch: bool
    Launch_system_LIM_Launch: bool
    Launch_system_LSM_Launch: bool
    Launch_system_Other: bool
    Launch_system_Other_Launch: bool
    Launch_system_Pneumatic_Launch: bool
    Launch_system_Powered_Coaster: bool
    Launch_system_Spiral_lift: bool
    Launch_system_Tire_Drive_system: bool

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[
        data.Length_ft,
        data.Location,
        data.Type,
        data.Manufacturer,
        data.Height_ft,
        data.Duration_sec,
        data.opening_date,
        data.Inversions,
        data.Launch_system_Elevator_lift,
        data.Launch_system_Hydraulic_Launch,
        data.Launch_system_LIM_Launch,
        data.Launch_system_LSM_Launch,
        data.Launch_system_Other,
        data.Launch_system_Other_Launch,
        data.Launch_system_Pneumatic_Launch,
        data.Launch_system_Powered_Coaster,
        data.Launch_system_Spiral_lift,
        data.Launch_system_Tire_Drive_system
    ]])
    
    prediction = model.predict(features)[0]
    return {"predicted_speed_mph": float(prediction)}
