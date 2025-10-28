from datetime import datetime
from typing import Optional
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


