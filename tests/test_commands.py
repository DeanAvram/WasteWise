from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER, start_test, next_sub_test, end_loop, end_test

resource_path = Path(__file__).parent / 'resources'


def test_create_command(client):
    counter: int = 1
    success: int = 0
    length: int = 0
    data: dict = {}

    data, length = start_test(data, length, 'create_command.json', 'test_create_command')

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
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 5) Got response {response}')
        LOGGER.info(f' 6) Got response {response.json}')
        answer = response.status_code == cmd['status_code']
        LOGGER.info(f' 7) comparison is {answer} - {response.status_code} == {cmd["status_code"]}')
        try:
            assert answer
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        counter, success = end_loop(counter, success)
    end_test(success, length)



