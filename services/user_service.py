from model import User

users=[

    User(id=1,name="Akshu",age=20,email="akshuchitra2006@gmail.com"),
    User(id=2,name="Shan",age=25,email="shan@gmail.com")

]

def get_all_users():
    return users

def get_user_id(id:int):
    for user in users:
        if user.id ==id:
            return user
        
def add_users(user:User):
    users.append(user)
    return {"message":"Added user successfully"}

def update_users(id:int,user:User):
    for i in range(len(users)):
        if users[i].id==id:
            users[i]=user
            return {"message":"user added successfully"}
    return{"error":"user not found"}

def delete_user(id:int):
    for i in range(len(users)):
        if users[i].id==id:
            del users[i]
            return {"message":"User deleted successfully"}
    return {"error":"user not found"}


