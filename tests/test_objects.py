from pathlib import Path
from http import HTTPStatus
from tests.conftest import get_test_data, equal_dicts_exclude, equal_dicts_only, LOGGER


resource_path = Path(__file__).parent / 'resources'

    
def test_create_object(client):
    counter: int = 1

    LOGGER.info('Starting test_create_object')
    data = get_test_data('create_object.json')
    LOGGER.info('1) Got test data')
    LOGGER.info(f'2) Got {len(data["tasks"])} tasks')

    LOGGER.info('3) Starting loop\n')
    for obj in data['tasks']:
        LOGGER.info(f'3.1) Starting create object Test {counter}')
        LOGGER.info(f'3.2) Posting {obj["object"]} to {obj["path"]}')
        path = obj['path']
        response = client.post(
            f'{path}?email=user@gmail.com',
            json=obj['object']
        )
        LOGGER.info(f'3.3) Got response {response}')
        LOGGER.info(f'3.3) Got response {response.json}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f'3.4) comparison is {answer}')
        assert answer

        LOGGER.info(f'3.5) Checking if test {counter} is valid')
        if response.status_code == HTTPStatus.CREATED:
            LOGGER.info(f'3.5.1) Comparing {response.json} to {obj["object"]}')
            answer = equal_dicts_only(response.json, obj['object'], 'type')
            LOGGER.info(f'3.5.2) comparison is {answer}')
            assert answer

            LOGGER.info(f'3.5.3) Checking if test {counter} has data')
            if 'data' in obj['object']:
                LOGGER.info(f'3.5.3.1) Comparing {response.json} to {obj["object"]}')
                answer = equal_dicts_exclude(response.json, obj['object'], '_id', 'created_by')
                LOGGER.info(f'3.5.3.1) comparison is {answer}')
                assert answer
        LOGGER.info(f'3.6 Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_create_object\n\n')
            
    
def test_get_object(client):
    counter: int = 1
    LOGGER.info('1) Starting test_get_object')
    data = get_test_data('get_object.json')
    LOGGER.info('2) Got test data')
    LOGGER.info(f'3) Got {len(data["tasks"])} tasks')

    LOGGER.info('4 Starting loop\n')
    for obj in data['tasks']:
        LOGGER.info(f'4.1) Starting Test {counter}')
        LOGGER.info(f'4.2) Posting {obj["object"]} to {obj["path"]}')
        path = obj['path']
        response = client.post(
            f'{path}?email=user@gmail.com',
            json=obj['object']
        )
        LOGGER.info(f'4.3) Got response {response}')
        LOGGER.info(f'4.3) Got response {response.json}')
        answer = response.status_code == HTTPStatus.CREATED
        LOGGER.info(f'4.4) comparison is {answer}')
        assert answer

        temp_id: str = response.json['_id']
        LOGGER.info(f'4.5) Got id {temp_id}')
        LOGGER.info(f'4.6) Checking if test {counter} is valid')
        if not obj['valid']:
            LOGGER.info(f'4.6.1) Test {counter} is invalid')
            LOGGER.info(f'4.6.2) temp_id is {temp_id} = {obj["id"]} obj["id"]')
            temp_id = obj['id']

        LOGGER.info(f'4.7) Getting {obj["path"]}/{temp_id}')
        path = f'{obj["path"]}/{temp_id}'
        response = client.get(
            f'{path}?email=user@gmail.com',
        )
        LOGGER.info(f'4.8) Got response {response}')
        LOGGER.info(f'4.8) Got response {response.json}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f'4.9) comparison is {answer}')
        assert answer

        LOGGER.info(f'4.10) Checking if test {counter} is valid')
        if not obj['valid']:
            LOGGER.info(f'4.10.1) Test {counter} is invalid')
            LOGGER.info(f'4.10.2) Loop {counter} done\n')
            continue

        LOGGER.info(f'4.11) Comparing {response.json} to {obj["object"]}')
        answer = equal_dicts_only(response.json, obj['object'], 'type')
        LOGGER.info(f'4.12) comparison is {answer}')
        assert answer

        LOGGER.info(f'4.13) Checking if test {counter} has data')
        if 'data' in obj['object']:
            LOGGER.info(f'4.13.1) Test {counter} has data')
            LOGGER.info(f'4.13.2) Comparing {response.json} to {obj["object"]}')
            answer = equal_dicts_only(response.json, obj['object'], 'type', 'data')
            LOGGER.info(f'4.13.3) comparison is {answer}')
            assert answer
        LOGGER.info(f'4.14) Loop {counter} done\n')
        counter += 1
    LOGGER.info('5) Done test_get_object\n\n')


def test_update_object(client):
    counter: int = 1
    LOGGER.info('1) Starting test_update_object')
    LOGGER.info('2) Getting test data')
    data = get_test_data('update_object.json')

    LOGGER.info('3) Starting loop\n')
    for obj in data['tasks']:
        LOGGER.info(f'3.1) Starting Test {counter}')
        LOGGER.info(f'3.2) Posting {obj["old_object"]} to {obj["path"]}')
        # Post object
        path = obj['path']
        response = client.post(
            f'{path}?email=user@gmail.com',
            json=obj['old_object']
        )
        LOGGER.info(f'3.3) Got response {response}')
        LOGGER.info(f'3.3) Got response {response.json}')
        assert response.status_code == HTTPStatus.CREATED 

        # Put object
        LOGGER.info(f'3.4) Putting {obj["changes"]} to {obj["path"]}/{response.json["_id"]}')
        path = f'{obj["path"]}/{response.json["_id"]}'
        response = client.put(
            f'{path}?email=user@gmail.com',
            json=obj['changes']
        )
        LOGGER.info(f'3.5) Got response {response}')
        LOGGER.info(f'3.5) Got response {response.json}')
        LOGGER.info(f'3.6) Comparing response status code {response.status_code} to {HTTPStatus.NO_CONTENT}')
        if response.status_code != HTTPStatus.NO_CONTENT:
            LOGGER.info(f'3.6.1) Test {counter} is invalid')
            continue

        LOGGER.info(f'3.7) Checking if test status code is {obj["status_code"]}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f'3.8) comparison is {answer}')
        assert answer
        
        # Get Updated object
        LOGGER.info(f'3.9) Getting {path}')
        response = client.get(
            f'{path}?email=user@gmail.com',
        )

        LOGGER.info(f'3.10) Got response {response}')
        LOGGER.info(f'3.10) Got response {response.json}')
        assert response.status_code == HTTPStatus.OK
        LOGGER.info(f'3.11) Comparing {response.json} to {obj["new_object"]}')
        assert equal_dicts_exclude(response.json, obj['new_object'], '_id', 'created_by')
        LOGGER.info(f'3.12) Loop {counter} done\n')
        counter += 1
    LOGGER.info('4) Done test_update_object\n\n')
        
