from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel

#base schema pattern for our API responses

class DeveloperBase(BaseModel):
    developer_name: str
    developer_level: int
    developer_email: str


#creating records inherit from base - database auto generated dev ID, created at, and active status
class DeveloperCreate(DeveloperBase):
    pass


#response schema for API
class Developer(DeveloperBase):
    developer_id: int
    active: bool #boolean field to indicate if the developer is active or not
    created_at: datetime
    updated_at: datetime
    
    class Config: #configures pydantic to convert database models to API responses
        from_attributes = True


class ReleaseRequestBase(BaseModel):
    software_name: str
    software_version: str
    developer_id: int
    release_notes: Optional[str] = None

class ReleaseRequestCreate(ReleaseRequestBase):
    pass

class ReleaseRequestUpdate(BaseModel):
    software_name: Optional[str] = None
    software_version: Optional[str] = None
    release_notes: Optional[str] = None
    risk_level: Optional[Literal["low", "medium", "high"]] = None
    status: Optional[Literal["pending", "approved", "rejected"]] = None

class ReleaseRequest(ReleaseRequestBase):
    id: int
    risk_level: Literal["low", "medium", "high"]
    status: Literal["pending", "approved", "rejected"]
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True