from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTIme
from .db import Base

#structure for our SQL tables

class ReleaseRequests(Base):
    __tablename__ = "release_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    developer_name = Column(String, nullable=False)

    risk_level = Column(String, default="unknown")
    status = Column(String, deafualt="pending")

    created_at = Column(DateTime, default=datetime.utcnow)
