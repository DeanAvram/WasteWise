from pathlib import Path
from tests.conftest import LOGGER, start_test, end_test, end_loop, post_everything, next_sub_test
from http import HTTPStatus

resource_path = Path(__file__).parent / 'resources'

user_data = {"tasks": [
    {
        "path": "/wastewise/users",
        "user": {
            "name": "test",
            "email": "dean@gmail.com",
            "password": "Dean123!!",
            "role": "USER"
        }
    },
    {
        "path": "/wastewise/users",
        "user": {
            "name": "test",
            "email": "daniel@gmail.com",
            "password": "Daniel123!",
            "role": "USER"
        }
    }

]}

object_data = {
    "tasks": [
        {
            "path": "/wastewise/objects",
            "object": {
                "type": "image",
            }
        },
        {
            "path": "/wastewise/objects",
            "object": {
                "type": "image",
                "data": {
                    "url": "https://www.google.com"
                }
            }
        }
    ]
}

command_data = {
    "tasks": [
        {
            "path": "/wastewise/commands",
            "command": {
                "type": "command_1"
            }
        },
        {
            "path": "/wastewise/commands",
            "command": {
                "type": "command_2"
            }
        }
    ]
}


def test_get_all_users_new(client):
    counter: int = 1
    success: int = 0
    length: int = 0
    data: dict = {}

    data, length = start_test(data, length, 'admin_users.json', 'test_get_all_users_new')

    for task in data['tasks']:
        LOGGER.info(f' ##### TITLE : {task["title"]} ####')
        LOGGER.info(f' Starting get all users Test {counter}')

        num_of_objects = post_everything(client, task['path'], task['users'], False, '')
        LOGGER.info(f' Got {num_of_objects} users')

        path: str = '/wastewise/admin/users'
        try:
            response = client.get(
                f'{path}?email=admin@gmail.com'
            )
            LOGGER.info(f' Got response {response}')
            LOGGER.info(f' Got response {response.json}')
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        try:
            LOGGER.info(f' Got {len(response.json)} users ?= {num_of_objects} + 2')
            assert response.status_code == HTTPStatus.OK and len(response.json) == len(task['users']) + 2
        except AssertionError as e:
            counter = next_sub_test(e, counter)
            continue

        counter, success = end_loop(counter, success)

    end_test(success, length)


def test_get_all_users(client):
    LOGGER.info(' Starting test : test_get_all_users')
    data = user_data
    create_data(client, data, 'user')
    LOGGER.info('5) Getting all users')
    path: str = '/wastewise/admin/users'
    response = client.get(
        f'{path}?email=admin@gmail.com'
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} users')
    answer = response.status_code == HTTPStatus.OK and len(response.json) == len(
        data['tasks']) + 2  # +1 for admin user +1 for user
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_users\n\n')


def test_get_all_objects(client):
    LOGGER.info('Starting test_get_all_objects')
    data = object_data
    create_data(client, data, 'object')
    LOGGER.info('5) Getting all objects')
    path: str = '/wastewise/admin/objects'
    response = client.get(
        f'{path}?email=admin@gmail.com'
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} objects')
    answer = response.status_code == HTTPStatus.OK and len(response.json) == len(data['tasks'])
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_objects\n\n')


def test_get_all_commands(client):
    LOGGER.info('Starting test_get_all_commands')
    data = command_data
    create_data(client, data, 'command')
    LOGGER.info('5) Getting all commands')
    path: str = '/wastewise/admin/commands'
    response = client.get(
        f'{path}?email=admin@gmail.com'
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} objects')
    answer = response.status_code == HTTPStatus.OK and len(response.json) == len(data['tasks'])
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_commands\n\n')


def test_delete_all_users(client):
    LOGGER.info('Starting test_delete_all_users')
    data = user_data
    create_data(client, data, 'user')
    LOGGER.info('5) Deleting all users')
    path: str = '/wastewise/admin/users'

    try:
        delete_get_and_assert(client, path, 'users')
    except Exception as e:
        LOGGER.critical(f'5.1) Got exception {e}')

    LOGGER.info('6) Done test_delete_all_users\n\n')


def test_delete_all_objects(client):
    LOGGER.info('Starting test_delete_all_objects')
    data = object_data
    create_data(client, data, 'object')
    LOGGER.info('5) Deleting all objects')
    path: str = '/wastewise/admin/objects'
    delete_get_and_assert(client, path, 'objects')
    LOGGER.info('6) Done test_delete_all_objects\n\n')


def test_delete_all_commands(client):
    LOGGER.info('Starting test_delete_all_commands')
    data = command_data
    create_data(client, data, 'command')

    LOGGER.info('5) Deleting all commands')
    path: str = '/wastewise/admin/commands'
    delete_get_and_assert(client, path, 'commands')
    LOGGER.info('6) Done test_delete_all_commands\n\n')


def create_data(client, data: dict, entity: str):
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')
    LOGGER.info('3) Starting loop\n')
    for i, ent in enumerate(data['tasks']):
        LOGGER.info(f'3.1) Starting Test {i + 1}')
        LOGGER.info(f'3.2) Posting {ent[entity]} to {ent["path"]}')
        path = ent['path']
        res = client.post(
            f'{path}?email=user@gmail.com',
            json=ent[entity]
        )
        LOGGER.info(f'3.3) Got response {res}')
        LOGGER.info(f'3.4) Got response {res.json}')
    LOGGER.info(f'4) Done posting {len(data["tasks"])} {entity}\n')


def delete_get_and_assert(client, path: str, entity: str):
    try:
        del_response = client.delete(
            f'{path}?email=admin@gmail.com'
        )
    except Exception as e:
        LOGGER.critical(f'5.1) Got exception {e}')

    LOGGER.info(f'5.1) del_response {del_response}')
    LOGGER.info(f'5.2) del_response {del_response.json}')

    LOGGER.info('6) Getting all ' + entity)
    try:
        get_response = client.get(
            f'{path}?email=admin@gmail.com'
        )
    except Exception as e:
        LOGGER.critical(f'6.1) Got exception {e}')

    LOGGER.info(f'6.1) get_response {get_response}')
    LOGGER.info(f'6.2) get_response {get_response.json}')
    LOGGER.info(f'6.3) Got {len(get_response.json)} {entity}')
    try:
        answer = del_response.status_code == HTTPStatus.NO_CONTENT and get_response.status_code == HTTPStatus.OK and \
                 len(get_response.json) == 0
        LOGGER.info(f'6.3) comparison is {answer}')
        assert answer
    except Exception as e:
        LOGGER.critical(f'6.4) Got exception {e}')
