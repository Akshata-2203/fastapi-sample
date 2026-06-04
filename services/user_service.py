from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def add_users(db: Session, user: UserCreate):
    db_user = User(name=user.name, age=user.age, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_users(db: Session, id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user:
        db_user.name = user.name
        db_user.age = user.age
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}
