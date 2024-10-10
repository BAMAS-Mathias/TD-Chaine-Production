import pytest
from web import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    yield app.app.test_client()
