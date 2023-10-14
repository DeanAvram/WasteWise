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
    create_admin_user()
    create_user()

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


def create_user() -> dict:
    user = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user)
    return user


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

    answer = d1_filtered == d2_filtered
    return answer


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
    LOGGER.info(f' End Subtest {counter}\n')
    success += 1
    counter += 1
    objectService.db.objects.delete_many({})
    # userService.db.users.delete_many({})
    commandService.db.commands.delete_many({})
    return counter, success


def end_test(success, length):
    LOGGER.info(f' Succeeded: {success} of {length}\n\n')


def post_everything(client, path: str, data: list):
    LOGGER.info(f' Posting {len(data)} objects to {path}')
    counter: int = 1

    for i in data:
        response = client.post(
            path,
            json=i
        )
        LOGGER.info(f' Posted {counter} : {i}')
        LOGGER.info(f' Got response {counter} : {response.json}')

        try:
            assert response.status_code == HTTPStatus.CREATED
        except AssertionError as e:
            continue

        counter += 1

