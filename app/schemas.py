from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum

class WorkoutDifficulty(str, Enum):
    easy = 'easy'
    medium = 'medium'
    hard = 'hard'


class ExerciseCreate(BaseModel):
    title: str
    description: str | None = None


class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str