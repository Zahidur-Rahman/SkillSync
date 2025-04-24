# app/models/session.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
import enum

class SessionStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    completed = "completed"

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    requester_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    status = Column(Enum(SessionStatus), default=SessionStatus.pending)
    scheduled_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    requester = relationship("User", foreign_keys=[requester_id], back_populates="requested_sessions")
    provider = relationship("User", foreign_keys=[provider_id], back_populates="provided_sessions")
    skill = relationship("Skill", back_populates="sessions")
