from database import sessionlocal

def db_get():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
        