from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# the url format 'postgresql://<username>:<password>@<ip-address>/<hostname>/fastAPI database'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:diba1379@localhost/fastAPI database'

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

