# app/models/skill.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.user_skills import user_skills

class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    # Many-to-Many with User
    users = relationship("User", secondary=user_skills, back_populates="skills")

    # One-to-Many with Session
    sessions = relationship("Session", back_populates="skill")
