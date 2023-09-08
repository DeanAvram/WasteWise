from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER, equal_dicts_exclude

resource_path = Path(__file__).parent / 'resources'


def test_create_command(client):
    counter: int = 1

    LOGGER.info('Starting test_create_command')
    data = get_test_data('create_command.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for cmd in data['tasks']:
        LOGGER.info(f'3.1) Starting create command Test {counter}')
        LOGGER.info(f'3.2) Posting {cmd["command"]} to {cmd["path"]}')

        response = client.post(
            cmd['path'],
            json=cmd['command']
        )

        LOGGER.info(f'3.3) Got response {response}')
        LOGGER.info(f'3.3) Got response {response.json}')
        answer = response.status_code == cmd['status_code']
        LOGGER.info(f'3.4) comparison is {answer}')
        assert answer

        LOGGER.info(f'3.6 Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_create_command\n\n')



