from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base

SQLALCHEMY_DATABASE_URL =  f"postgresql://postgres:{settings.database_password}@localhost:5432/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# default values
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind= engine)
    Base.metadata.create_all(bind= engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()
    # command.upgrade(alembic_cfg, "head")
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # command.downgrade(alembic_cfg, "base")
