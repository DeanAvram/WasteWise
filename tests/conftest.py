from pathlib import Path
import pytest
import json
import os
import logging

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
    create_admin_user()
    create_user()

    yield


def create_admin_user():
    user = {
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "Testing193!",
        "role": "ADMIN"
    }
    userService.create_user(user)


def create_user():
    user = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user)


def get_test_data(filename) -> dict:
    folder_path = os.path.abspath(Path(os.path.dirname(__file__)))
    folder = os.path.join(folder_path, 'test_data')
    jsonfile = os.path.join(folder, filename)
    with open(jsonfile) as file:
        data = json.load(file)

    return data


def equal_dicts_exclude(d1, d2, *ignore_keys):
    d1_filtered = {k: v for k, v in d1.items() if k not in ignore_keys}
    d2_filtered = {k: v for k, v in d2.items() if k not in ignore_keys}
    return d1_filtered == d2_filtered


def equal_dicts_only(d1, d2, *keys):
    d1_filtered = {k: v for k, v in d1.items() if k in keys}
    d2_filtered = {k: v for k, v in d2.items() if k in keys}
    return d1_filtered == d2_filtered


def start_test(data, length, file, name):
    LOGGER.info(f' Starting: {name}')

    try:
        data = get_test_data(file)
        LOGGER.info(' Got test data')
    except Exception as e:
        LOGGER.error(f' Failing in get test data Got exception {e}')
        return

    length = len(data['tasks'])

    LOGGER.info(f' Got {length} tasks')

    LOGGER.info('')
    return data, length


def next_sub_test(e, counter):
    LOGGER.error(f' Failing in put object -> {e}')
    LOGGER.error(f' Failing test {counter}\n')
    counter += 1
    return counter


def end_loop(counter, success):
    LOGGER.info(f' End sub test{counter}\n')
    success += 1
    counter += 1
    return counter, success


def end_test(success, length):
    LOGGER.info(f' Succeeded: {success} of {length}\n\n')
