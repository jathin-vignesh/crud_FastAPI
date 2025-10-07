from sqlalchemy.orm import Session
from db import Base
from sqlalchemy import Column, Integer, String
from schemas.crud_schema import PersonCreate
from typing import List
from models.crud_models import Person as User

def create_user(db: Session, user: PersonCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session) -> List[User]:
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user: PersonCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
