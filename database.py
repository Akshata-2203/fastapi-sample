from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

URL_DATABASE="mysql+pymysql://root:ShAk@1222@localhost:3306/fastapi_db"

engine=create_engine(URL_DATABASE)

sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()