from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from services import crud_operations as crud
from schemas.crud_schema import PersonCreate, PersonResponse
from typing import List

router = APIRouter()

@router.post("/users", response_model=PersonResponse)
def create_user(user: PersonCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users", response_model=List[PersonResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/users/{user_id}", response_model=PersonResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=PersonResponse)
def update_user(user_id: int, user: PersonCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
