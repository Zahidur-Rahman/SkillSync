from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    
    is_active = Column(Boolean, default=True)

    # Relationship with skills (many-to-many)
    skills = relationship("Skill", secondary="user_skills", back_populates="users")

    # Relationship with sessions (one-to-many as requester or provider)
    requested_sessions = relationship("Session", foreign_keys="Session.requester_id", back_populates="requester")
    provided_sessions = relationship("Session", foreign_keys="Session.provider_id", back_populates="provider")
