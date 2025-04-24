# app/models/user_skills.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

user_skills = Table(
    "user_skills",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("skill_id", Integer, ForeignKey("skills.id"))
)
