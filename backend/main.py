from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from . import models, schemas

app = FastAPI(title="ShipSafe API", version="0.1.0")

# SQLAlchemy builds the models defined in models.py into the database (initializes the database)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health() -> dict:
    return {"status":"ok"}


@app.post("/developers", response_model=schemas.Developer, status_code=status.HTTP_201_CREATED)
def create_developer(developer: schemas.DeveloperCreate, db: Session = Depends(get_db))
