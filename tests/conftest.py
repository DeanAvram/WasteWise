from pathlib import Path
import pytest
import json
import os
import logging
from http import HTTPStatus

from src import create_app
from src.services.rest.object_service import ObjectService
from src.services.rest.user_service import UserService
from src.services.rest.command_service import CommandService

objectService = ObjectService()
userService = UserService()
commandService = CommandService()

LOGGER = logging.getLogger(__name__)
# write to file after clearing it
open('test.log', 'w').close()
logging.basicConfig(filename='test.log', level=logging.INFO)


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
    userService.db.users.delete_many({})
    commandService.db.commands.delete_many({})

    # add admin user
    # create_admin_user()
    # create_user("User", "user@gmail.com", "Testing193!", "USER")

    yield

    objectService.db.objects.delete_many({})
    userService.db.users.delete_many({})
    commandService.db.commands.delete_many({})


def create_admin_user() -> dict:
    user = {
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "Testing193!",
        "role": "ADMIN"
    }
    userService.create_user(user)
    return user


def create_user(username: str, email: str, password: str, role: str) -> dict:
    user = {
        "name": username,
        "email": email,
        "password": password,
        "role": role
    }
    userService.create_user(user)

    return user


def create_object(client, name: str, description: str, location: str, owner: str) -> dict:
    temp_object = {
        "name": name,
        "description": description,
        "location": location,
        "owner": owner
    }

    response = client.post(
        '/wastewise/objects',
        json=temp_object
    )

    return response.json




def equal_dicts_only(d1, d2, *keys):
    d1_filtered = {k: v for k, v in d1.items() if k in keys}
    d2_filtered = {k: v for k, v in d2.items() if k in keys}

    answer = d1_filtered == d2_filtered
    return answer




