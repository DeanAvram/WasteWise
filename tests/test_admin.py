from pathlib import Path
from tests.conftest import get_test_data, LOGGER, equal_dicts_exclude

resource_path = Path(__file__).parent / 'resources'


def test_get_all_users(client):
    LOGGER.info('Starting test_get_all_users')
    data = get_test_data('get_all_users.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for i, usr in enumerate(data['tasks']):
        LOGGER.info(f'3.1) Starting Test {i + 1}')
        LOGGER.info(f'3.2) Posting {usr["user"]} to {usr["path"]}')
        response = client.post(
            usr['path'],
            json=usr['user']
        )
    LOGGER.info(f'4) Done posting {len(data["tasks"])} users\n')

    LOGGER.info('5) Getting all users')
    path: str = '/wastewise/admin/users'
    response = client.get(
        path
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} users')
    answer = response.status_code == 200 and len(response.json) == len(data['tasks'])
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_users\n\n')


def test_get_all_objects(client):
    LOGGER.info('Starting test_get_all_objects')
    data = get_test_data('get_all_objects.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for i, obj in enumerate(data['tasks']):
        LOGGER.info(f'3.1) Starting Test {i + 1}')
        LOGGER.info(f'3.2) Posting {obj["object"]} to {obj["object"]}')
        response = client.post(
            obj['path'],
            json=obj['object']
        )
    LOGGER.info(f'4) Done posting {len(data["tasks"])} objects\n')

    LOGGER.info('5) Getting all objects')
    path: str = '/wastewise/admin/objects'
    response = client.get(
        path
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} objects')
    answer = response.status_code == 200 and len(response.json) == len(data['tasks'])
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_users\n\n')


def test_get_all_commands(client):
    LOGGER.info('Starting test_get_all_commands')
    data = get_test_data('get_all_commands.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for i, com in enumerate(data['tasks']):
        LOGGER.info(f'3.1) Starting Test {i + 1}')
        LOGGER.info(f'3.2) Posting {com["command"]} to {com["command"]}')
        response = client.post(
            com['path'],
            json=com['command']
        )
    LOGGER.info(f'4) Done posting {len(data["tasks"])} commands\n')

    LOGGER.info('5) Getting all commands')
    path: str = '/wastewise/admin/commands'
    response = client.get(
        path
    )
    LOGGER.info(f'5.1) Got response {response}')
    LOGGER.info(f'5.2) Got response {response.json}')
    LOGGER.info(f'5.3) Got {len(response.json)} objects')
    answer = response.status_code == 200 and len(response.json) == len(data['tasks'])
    LOGGER.info(f'5.3) comparison is {answer}')
    assert answer
    LOGGER.info('6) Done test_get_all_commands\n\n')




