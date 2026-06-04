from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import User
from services.user_service import (
    get_all_users,
    add_users,
    update_users,
    delete_user,
    get_user_id
)
from db_dependency import get_db

router = APIRouter()

@router.get("/")
def greet():
    return {"message": "USER DETAILS"}

@router.get("/users")
def get_user(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{id}")
def get_id(id: int, db: Session = Depends(get_db)):
    return get_user_id(db, id)

@router.post("/users")
def add(user: User, db: Session = Depends(get_db)):
    return add_users(db, user)

@router.put("/users/{id}")
def upuser(id: int, user: User, db: Session = Depends(get_db)):
    return update_users(db, id, user)

@router.delete("/users/{id}")
def deluser(id: int, db: Session = Depends(get_db)):
    return delete_user(db, id)
