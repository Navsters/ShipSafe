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
def create_developer(developer: schemas.DeveloperCreate, db: Session = Depends(get_db)):

    if db.query(models.Developer).filter(models.Developer.developer_email == developer.developer_email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Developer already exists")
    
    db_developer = models.Developer(
        developer_name=developer.developer_name,
        developer_level=developer.developer_level,
        developer_email=developer.developer_email
    )
    db.add(db_developer)
    db.commit()
    db.refresh(db_developer)
    return db_developer

@app.get("/developers", response_model=list[schemas.Developer])
def get_developers(db: Session = Depends(get_db)):
    developers = db.query(models.Developer).all()
    return developers

@app.get("/developers/{developer_id}", response_model=schemas.Developer)
def get_developer(developer_id: int, db: Session = Depends(get_db)):
    db_developer = db.query(models.Developer).filter(models.Developer.developer_id == developer_id).first()
    if db_developer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    return db_developer

@app.put("/developers/{developer_id}", response_model=schemas.Developer)
def update_developer(developer_id: int, developer: schemas.DeveloperCreate, db: Session = Depends(get_db)):
    db_developer = db.query(models.Developer).filter(models.Developer.developer_id == developer_id).first()
    if db_developer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    db_developer.developer_name = developer.developer_name
    db_developer.developer_level = developer.developer_level
    db_developer.developer_email = developer.developer_email
    db.commit()
    db.refresh(db_developer)
    return db_developer

@app.delete("/developers/{developer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_developer(developer_id: int, db: Session = Depends(get_db)):
    db_developer = db.query(models.Developer).filter(models.Developer.developer_id == developer_id).first()
    if db_developer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    db.delete(db_developer)
    db.commit()
    return

@app.post("/releases", response_model=schemas.ReleaseRequest, status_code=status.HTTP_201_CREATED)
def create_release_request(release: schemas.ReleaseRequestCreate, db: Session = Depends(get_db)):
    # Check if developer exists
    developer = db.query(models.Developer).filter(models.Developer.developer_id == release.developer_id).first()
    if developer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    db_release = models.ReleaseRequest(
        software_name=release.software_name,
        software_version=release.software_version,
        developer_id=release.developer_id,
        release_notes=release.release_notes,
        risk_level="unknown",  # Will be set by policy engine later
        status="pending"
    )
    db.add(db_release)
    db.commit()
    db.refresh(db_release)
    return db_release


@app.get("/releases", response_model=list[schemas.ReleaseRequest])
def get_release_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all release requests with pagination"""
    releases = db.query(models.ReleaseRequest).offset(skip).limit(limit).all()
    return releases


@app.get("/releases/{release_id}", response_model=schemas.ReleaseRequest)
def get_release_request(release_id: int, db: Session = Depends(get_db)):
    """Get a specific release request by ID"""
    db_release = db.query(models.ReleaseRequest).filter(models.ReleaseRequest.id == release_id).first()
    if db_release is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release request not found")
    return db_release


@app.put("/releases/{release_id}", response_model=schemas.ReleaseRequest)
def update_release_request(
    release_id: int,
    release_update: schemas.ReleaseRequestUpdate,
    db: Session = Depends(get_db)
):
    """Update a release request - only updates fields that are provided"""
    db_release = db.query(models.ReleaseRequest).filter(models.ReleaseRequest.id == release_id).first()
    if db_release is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release request not found")
    
    # Update only the fields that were provided in the request
    update_data = release_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_release, field, value)
    
    db.commit()
    db.refresh(db_release)
    return db_release


@app.delete("/releases/{release_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_release_request(release_id: int, db: Session = Depends(get_db)):
    """Delete a release request"""
    db_release = db.query(models.ReleaseRequest).filter(models.ReleaseRequest.id == release_id).first()
    if db_release is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release request not found")
    
    db.delete(db_release)
    db.commit()
    return

