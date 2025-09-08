"""Pytest configuration and shared fixtures."""

import pytest
from typing import Generator
import tempfile
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

# This will be imported once we create the main app
# from src.real_estate_tracker.api.main import app
# from src.real_estate_tracker.models.database import Base, get_db


@pytest.fixture(scope="session")
def test_db() -> Generator[str, None, None]:
    """Create a temporary database for testing."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        test_db_url = f"sqlite:///{tmp.name}"
        yield test_db_url
    
    # Cleanup
    if os.path.exists(tmp.name):
        os.unlink(tmp.name)


@pytest.fixture(scope="function")
def db_session(test_db: str):
    """Create a database session for testing."""
    engine = create_engine(test_db, connect_args={"check_same_thread": False})
    # Base.metadata.create_all(bind=engine)
    
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="function")
def client(db_session) -> TestClient:
    """Create a test client for the API."""
    # def override_get_db():
    #     return db_session
    
    # app.dependency_overrides[get_db] = override_get_db
    # return TestClient(app)
    pass


@pytest.fixture
def sample_property_data():
    """Sample property data for testing."""
    return {
        "address": "123 Main St, Lafayette, CO 80026",
        "price": 750000,
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 2100,
        "lot_size": 0.25,
        "year_built": 2015,
        "property_type": "Single Family",
        "listing_status": "Active",
        "days_on_market": 15,
        "mls_number": "12345678",
        "zip_code": "80026"
    }


@pytest.fixture
def sample_user_preferences():
    """Sample user preferences for testing."""
    return {
        "name": "Test User",
        "age": 30,
        "current_address": "456 Test Ave, Boulder, CO 80301",
        "min_bedrooms": 3,
        "min_bathrooms": 2,
        "min_square_feet": 1800,
        "max_square_feet": 2500,
        "min_price": 600000,
        "max_price": 1000000,
        "zip_codes": ["80026", "80027", "80301"],
        "preferred_landmarks": ["park", "lake"]
    }


@pytest.fixture
def mock_api_response():
    """Mock API response for external real estate APIs."""
    return {
        "listings": [
            {
                "zpid": "123456789",
                "address": "123 Test St, Lafayette, CO 80026",
                "price": 725000,
                "bedrooms": 3,
                "bathrooms": 2,
                "living_area": 2000,
                "property_type": "SINGLE_FAMILY",
                "home_status": "FOR_SALE",
                "days_on_zillow": 10
            }
        ]
    }


# Test data directory
@pytest.fixture
def test_data_dir() -> Path:
    """Path to test data directory."""
    return Path(__file__).parent / "data"


# Environment variables for testing
@pytest.fixture(autouse=True)
def test_environment(monkeypatch):
    """Set up test environment variables."""
    monkeypatch.setenv("ENVIRONMENT", "testing")
    monkeypatch.setenv("DEBUG", "True")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/1")  # Use DB 1 for testing