import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app import crud
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

ALGORITHM = os.getenv('ALGORITHM')

ACCESS_TOKEN_EXPIRES_MINUTES=int(os.getenv('ACCESS_TOKEN_EXPIRES_MINUTES'))