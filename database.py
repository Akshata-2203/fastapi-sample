from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base #basemodel  

URL_DATABASE="mysql+mysqlconnector://root:ShAk%401222@localhost:3306/fastapi_db"

engine=create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()