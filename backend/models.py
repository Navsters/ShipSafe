from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Index
from .db import Base

#structure for our SQL tables

class ReleaseRequest(Base):
    __tablename__ = "release_request"

    id = Column(Integer, primary_key=True, index=True)
    software_name = Column(String, nullable=False)
    software_version = Column(String, nullable=False)
    developer_id = Column(Integer, ForeignKey("developer_information.developer_id"), index=True,nullable=False)
    release_notes = Column(String)

    risk_level = Column(String, default="unknown")
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.now)


class Developer(Base):
    __tablename__ = "developer_information"

    developer_id = Column(Integer, primary_key=True, index=True, unique=True)
    developer_name=Column(String, nullable=False, unique=True)
    developer_level=Column(Integer,nullable=False, index=True)
    developer_email=Column(String, nullable=False, unique=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

class Approval(Base):
    __tablename__ = "approval"

    approval_id = Column(Integer, primary_key=True, index=True)
    release_request_id = Column(Integer, ForeignKey("release_request.id"), index=True,nullable=False)
    reviewer_id = Column(Integer, ForeignKey("developer_information.developer_id"), index=True, nullable=False)
    aproval_status = Column(String, default="pending")
    approval_decision = Column(Boolean, nullable=False)
    approval_timestamp = Column(DateTime, default=datetime.now)
    approval_notes = Column(String)

class AuditLog(Base):
    __tablename__ = "audit_log"

    audit_log_id = Column(Integer, primary_key=True, index=True)
    release_request_id = Column(Integer, ForeignKey("release_request.id"), index=True, nullable=False)
    action = Column(String, nullable=False)
    actor_id = Column(Integer, ForeignKey("developer_information.developer_id"), index=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)


