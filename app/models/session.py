from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    requester_id = Column(Integer, ForeignKey("users.id"))
    provider_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    status = Column(String, default="pending")  # pending, accepted, completed
    scheduled_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    requester = relationship("User", foreign_keys=[requester_id])
    provider = relationship("User", foreign_keys=[provider_id])
    skill = relationship("Skill")
