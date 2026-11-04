from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import os

app = FastAPI()

# --- 1. Pydantic Model ---
class PatientData(BaseModel):
    name: str
    age: int

# --- 2. Helper Functions (The File Cabinet) ---
DB_FILE = "patients.json"

def load_data():
    """Reads the JSON file. If it doesn't exist, returns an empty list."""
    if not os.path.exists(DB_FILE):
        return []  # Start with an empty list if file is missing

    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """Saves the updated list of patients back to the JSON file."""
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)  # indent=4 makes it readable

# --- 3. Serve HTML Pages ---
@app.get("/")
def serve_home():
    return FileResponse("index.html")

@app.get("/form-page")
def serve_form():
    return FileResponse("form.html")

# --- 4. Receive and SAVE Form Data ---
@app.post("/submit-data")
def submit_data(patient: PatientData):
    # A. Load existing patients
    all_patients = load_data()

    # B. Add the new patient (convert Pydantic model to dictionary)
    all_patients.append(patient.model_dump())

    # C. Save back to the file
    save_data(all_patients)

    print(f"Saved to file: {patient.name}, Age: {patient.age}")

    return {
        "status": "success",
        "message": f"Successfully saved {patient.name} to the database file!"
    }
