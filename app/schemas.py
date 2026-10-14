from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class WorkoutDificulty(str, Enum):
    easy = 'easy'
    medium = 'medium'
    hard = 'hard'


class ExerciseCreate(BaseModel):
    title: str
    description: str


class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str