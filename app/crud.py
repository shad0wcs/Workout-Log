from sqlalchemy.orm import Session
from models import User, Exercise, Workout
from app.schemas import UserCreate, ExerciseCreate
from app.auth import hash_password


def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)
    db_user = User(email = user.email, hash_password = hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = Exercise(title = exercise.title, description = exercise.description)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise
