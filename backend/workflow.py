from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.orm import Session
from . import models

def approve_existing_release(payload, db: Session):
    existing_release = db.query(models.ReleaseRequest).filter(
        models.ReleaseRequest.id == payload.release_request_id
    ).first()
    
    if not existing_release:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Release request not found, please create a new release request")

    if existing_release.developer_id == payload.developer_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to approve this release request")

    reviewer = db.query(models.Developer).filter(
        models.Developer.developer_id == payload.developer_id
    ).first()
    
    submitter = db.query(models.Developer).filter(
        models.Developer.developer_id == existing_release.developer_id
    ).first()
    
    if not reviewer or not submitter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found")
    
    if reviewer.developer_level < submitter.developer_level:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="A more senior Developer must approve this release request")

    existing_release.status = "approved"
    existing_release.updated_at = datetime.now()
    existing_release.reviewer_id = payload.developer_id
    db.commit()
    db.refresh(existing_release)
    return existing_release
