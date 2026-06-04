from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_dependency import get_db
from services.user_service import (
    get_all_users,
    add_users,
    update_users,
    delete_user,
    get_user_id
)
from schemas import UserCreate, UserResponse

router = APIRouter()

@router.get("/")
def greet():
    return {"message": "USER DETAILS"}

@router.get("/users", response_model=list[UserResponse])
def get_user(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{id}", response_model=UserResponse)
def get_id(id: int, db: Session = Depends(get_db)):
    user = get_user_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserResponse)
def add(user: UserCreate, db: Session = Depends(get_db)):
    return add_users(db, user)

@router.put("/users/{id}", response_model=UserResponse)
def upuser(id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated = update_users(db, id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/users/{id}")
def deluser(id: int, db: Session = Depends(get_db)):
    return delete_user(db, id)
