import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("🎢 Roller Coaster Speed Predictor (v2)")
st.write("Enter coaster details to predict speed (mph).")

# Numeric inputs
Length_ft = st.number_input("Length (ft)", 0.0)
Location = st.number_input("Location (encoded)", 0.0)
Type = st.number_input("Type (encoded)", 0.0)
Manufacturer = st.number_input("Manufacturer (encoded)", 0.0)
Height_ft = st.number_input("Height (ft)", 0.0)
Duration_sec = st.number_input("Duration (sec)", 0.0)
opening_date = st.number_input("Opening Date (year)", 1900.0, 2025.0)
Inversions = st.number_input("Inversions", 0.0)

# Boolean inputs (launch systems)
Launch_system_Elevator_lift = st.checkbox("Elevator lift")
Launch_system_Hydraulic_Launch = st.checkbox("Hydraulic Launch")
Launch_system_LIM_Launch = st.checkbox("LIM Launch")
Launch_system_LSM_Launch = st.checkbox("LSM Launch")
Launch_system_Other = st.checkbox("Other")
Launch_system_Other_Launch = st.checkbox("Other Launch")
Launch_system_Pneumatic_Launch = st.checkbox("Pneumatic Launch")
Launch_system_Powered_Coaster = st.checkbox("Powered Coaster")
Launch_system_Spiral_lift = st.checkbox("Spiral lift")
Launch_system_Tire_Drive_system = st.checkbox("Tire/Drive system")

if st.button("Predict"):
    payload = {
        "Length_ft": Length_ft,
        "Location": Location,
        "Type": Type,
        "Manufacturer": Manufacturer,
        "Height_ft": Height_ft,
        "Duration_sec": Duration_sec,
        "opening_date": opening_date,
        "Inversions": Inversions,
        "Launch_system_Elevator_lift": Launch_system_Elevator_lift,
        "Launch_system_Hydraulic_Launch": Launch_system_Hydraulic_Launch,
        "Launch_system_LIM_Launch": Launch_system_LIM_Launch,
        "Launch_system_LSM_Launch": Launch_system_LSM_Launch,
        "Launch_system_Other": Launch_system_Other,
        "Launch_system_Other_Launch": Launch_system_Other_Launch,
        "Launch_system_Pneumatic_Launch": Launch_system_Pneumatic_Launch,
        "Launch_system_Powered_Coaster": Launch_system_Powered_Coaster,
        "Launch_system_Spiral_lift": Launch_system_Spiral_lift,
        "Launch_system_Tire_Drive_system": Launch_system_Tire_Drive_system
    }

    try:
        response = requests.post(f"{API_URL}/predict", json=payload)
        if response.status_code == 200:
            st.success(f"Predicted Speed: {response.json()['predicted_speed_mph']} mph")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
