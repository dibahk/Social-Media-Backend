from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

# the url format 'postgresql://<username>:<password>@<ip-address>/<hostname>/fastAPI database'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# while True:
#     try:
#         conn = psycopg2.connect(host= 'localhost', database= 'fastAPI database', user= 'postgres', password= 'diba1379', cursor_factory=RealDictCursor) #readdictcursor gonna give the column names.
#         cursor = conn.cursor() # for executing sql statemenets
#         print('database connection was successful')
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# default values
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

