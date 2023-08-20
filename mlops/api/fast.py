import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from mlops.ml_logic.registry import load_model
from mlops.interface.main import fast_pred
import uuid

from mlops.params import *

app = FastAPI()
model = load_model()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/image_predict/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    #save the file
    with open(f"{SAVEIMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    prediction = fast_pred(model, f"{SAVEIMAGEDIR}{file.filename}")

    return {"filename": file.filename, "prediction": ",".join(prediction)}

@app.get("/")
def root():
    return {'greeting': 'Hello'}