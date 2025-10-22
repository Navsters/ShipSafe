from fastapi import FastAPI
from .db import Base, engine

app = FastAPI(title="ShipSafe API", version="0.1.0")

# SQLAlchemy builds the models defined in models.py into the database (initializes the database)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health() -> dict:
    return {"status":"ok"}

