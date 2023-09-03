from pathlib import Path
import pytest
import json
import os

from src import create_app
from src.services.object_service import ObjectService


objectService = ObjectService()


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            'TESTING': True,
        }
    )
    
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def before_and_after_test():
    # clear database before each test
    objectService.db.objects.delete_many({}) 

    yield

def get_test_data(filename) -> dict:
    folder_path = os.path.abspath(Path(os.path.dirname(__file__)))
    folder = os.path.join(folder_path, 'test_data')
    jsonfile = os.path.join(folder, filename)
    with open(jsonfile) as file:
        data = json.load(file)

    return data