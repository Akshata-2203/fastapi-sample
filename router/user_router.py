from fastapi import APIRouter
from model import User
from services.user_service import (
        get_all_users, 
        add_users,
        update_users,
        delete_user,
        get_user_id
)

router=APIRouter()


@router.get("/")
def greet():
    return {"message":"USER DETAILS"}

@router.get("/users")
def get_user():
    return get_all_users()

@router.get("/users/{id}")
def get_id(id:int):
    return get_user_id(id)


@router.post("/users")
def add(user:User):
    return add_users(user)

@router.put("/users")
def upuser(id:int,user:User):
    return update_users(id,user)

@router.delete("/users")
def deluser(id:int):
    return delete_user(id)