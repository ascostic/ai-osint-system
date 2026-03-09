from fastapi import FastAPI, UploadFile, File
from modules.metadata_extractor import extract_gps
import shutil
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI-OSINT System Running"}

@app.post("/extract-gps")
async def extract_gps_endpoint(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = f"data/temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run extraction
    result = extract_gps(temp_path)

    # Clean up temp file
    os.remove(temp_path)

    if result is None:
        return {"error": "No GPS data found in this image"}

    return result