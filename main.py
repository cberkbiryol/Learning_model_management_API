# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4, UUID
from datetime import datetime
from typing import List, final

from starlette.status import HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE

app = FastAPI()


class Model(BaseModel):
    id: UUID
    name: str
    version: str
    created_at: datetime


class ModelCreate(BaseModel):
    name: str
    version: str = ""

# Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Model Registry API is running"}

models = []  # In-memory store

# Endpoint for adding new models
@app.post("/models", response_model=Model)
def register_model(model_create: ModelCreate):
    """
    Register a new machine learning model with a generated UUID and timestamp.
    """
    this_name = [m for m in models if m.name == model_create.name]
    version = model_create.version
    final_version = model_create.version if version else "1.0.0"
    if len(this_name) > 0:
        if version:
            this_vers = [m for m in this_name if m.version == model_create.version]
            if len(this_vers) > 0:
                raise HTTPException(409, detail=f"There is already a model with name {model_create.name} and"
                                                f" model version {model_create.version}")
            else:
                final_version = model_create.version
        else:
            versions = [m.version for m in this_name]
            versions.sort()
            last_version = versions[-1]
            major, minor, patch = map(int, last_version.split("."))
            final_version = f"{major}.{minor}.{patch+1}"

    model = Model(
        id=uuid4(),
        name=model_create.name,
        version=final_version,
        created_at=datetime.utcnow()
    )
    models.append(model)
    return model

# Endpoint for retrieving all models
@app.get("/models", response_model=List[Model])
def list_models():
    return models

# Endpoint for retrieving specific model with the given model_id
@app.get("/models/{model_id}", response_model=Model)
def get_model_by_id(model_id: UUID):
    """
    Retrieve a model from the in-memory registry using its UUID.
    """
    for model in models:
        if model.id == model_id:
            return model
    raise HTTPException(status_code=404, detail="Model not found")