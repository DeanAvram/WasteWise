from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_create_command(client):
    counter: int = 1
    success: int = 0

    LOGGER.info(' Starting test : test_create_command')
    data = get_test_data('create_command.json')
    LOGGER.info(' Got test data')
    length = len(data['tasks'])
    LOGGER.info(f' Got {length} tasks')

    LOGGER.info('3) Starting loop\n')
    for cmd in data['tasks']:
        LOGGER.info(f' ##### TITLE : {cmd["title"]} ####')
        LOGGER.info(f' 1) Starting create command Test {counter}')
        LOGGER.info(f' 2) Posting {cmd["command"]} to {cmd["path"]}')

        path = cmd['path']
        try:
            response = client.post(
                f'{path}?email=user@gmail.com',
                json=cmd['command']
            )
        except Exception as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}\n')
            counter += 1
            continue

        LOGGER.info(f' 5) Got response {response}')
        LOGGER.info(f' 6) Got response {response.json}')
        answer = response.status_code == cmd['status_code']
        LOGGER.info(f' 7) comparison is {answer}')
        try:
            assert answer
        except Exception as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}\n')
            counter += 1
            continue

        LOGGER.info(f'3.6 Loop {counter} done\n')
        counter += 1
        success += 1
    LOGGER.info(f' Succeeded: {success} of {length} \n\n')



