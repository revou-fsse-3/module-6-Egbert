from app import app
import pytest

@pytest.fixture
def test_app():
    app.config['Testing'] = True

    with app.test_client() as client:
        yield client