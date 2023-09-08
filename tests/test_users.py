from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER, equal_dicts_exclude

resource_path = Path(__file__).parent / 'resources'


def test_create_user(client):
    counter: int = 1

    LOGGER.info('Starting test_create_user')
    data = get_test_data('create_user.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for usr in data['tasks']:
        LOGGER.info(f'3.1) Starting create user Test {counter}')
        LOGGER.info(f'3.2) Posting {usr["user"]} to {usr["path"]}')
        response = client.post(
            usr['path'],
            json=usr['user']
        )
        LOGGER.info(f'3.3) Got response {response}')
        LOGGER.info(f'3.3) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f'3.4) comparison is {answer}')
        assert answer

        if response.status_code == HTTPStatus.CREATED:
            LOGGER.info(f'3.5.1) Comparing {response.json} to {usr["user"]}')
            answer = equal_dicts_exclude(response.json, usr['user'], '_id')
            LOGGER.info(f'3.5.2) comparison is {answer}')
            assert answer

        LOGGER.info(f'3.6 Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_create_user\n\n')


def test_get_user(client):
    counter: int = 1
    LOGGER.info('Starting test_get_user')
    data = get_test_data('get_user.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for usr in data['tasks']:
        LOGGER.info(f'3.1) Starting get user Test {counter}')
        LOGGER.info(f'3.2) Posting {usr["user"]} to {usr["path"]}')
        response = client.post(
            usr['path'],
            json=usr['user']
        )
        LOGGER.info(f'3.3) Got response {response}')

        # get user
        LOGGER.info(f'3.4) Getting user {usr["user"]["email"]}')
        path: str = usr['path'] + '/' + usr['user']['email']
        response = client.get(
            path
        )
        LOGGER.info(f'3.5) Got response {response}')
        LOGGER.info(f'3.6) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f'3.7) comparison is {answer}')
        assert answer
        LOGGER.info(f'3.8) Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_create_user\n\n')


def test_update_user(client):
    counter: int = 1
    LOGGER.info('Starting test_update_user')
    data = get_test_data('update_user.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for usr in data['tasks']:
        LOGGER.info(f'3.1) Starting update user Test {counter}')
        LOGGER.info(f'3.2) Posting {usr["old_user"]} to {usr["path"]}')
        response = client.post(
            usr['path'],
            json=usr['old_user']
        )
        LOGGER.info(f'3.3) Got response {response}')

        # update user
        LOGGER.info(f'3.4) Updating user {usr["old_user"]["email"]}')
        path: str = usr['path'] + '/' + usr['old_user']['email']
        response = client.put(
            path,
            json=usr['changes']
        )
        LOGGER.info(f'3.5) Got response {response}')
        LOGGER.info(f'3.6) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f'3.7) comparison is {answer}')
        assert answer

        if response.status_code == HTTPStatus.OK:
            LOGGER.info(f'3.8.1) Comparing {response.json} to {usr["new_user"]}')
            answer = equal_dicts_exclude(response.json, usr['new_user'], '_id')
            LOGGER.info(f'3.8.2) comparison is {answer}')
            assert answer
