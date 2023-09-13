from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER

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

        path = cmd['path']
        try:
            response = client.post(
                f'{path}?email=user@gmail.com',
                json=cmd['command']
            )
        except Exception as e:
            LOGGER.fatal(f'3.2) Got exception {e}\n')
            counter += 1
            continue

        LOGGER.info(f'3.3) Got response {response}')
        LOGGER.info(f'3.3) Got response {response.json}')
        answer = response.status_code == cmd['status_code']
        LOGGER.info(f'3.4) comparison is {answer}')
        try:
            assert answer
        except Exception as e:
            LOGGER.fatal(f'3.4) Got exception {e}\n')
            counter += 1
            continue

        LOGGER.info(f'3.6 Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_create_command\n\n')



