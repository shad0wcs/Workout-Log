from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=True)


class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    difficulty = Column(String, nullable=False, default='medium')
