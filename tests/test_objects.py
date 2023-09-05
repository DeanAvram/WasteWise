from pathlib import Path
from http import HTTPStatus
from tests.conftest import get_test_data, equal_dicts_exclude, equal_dicts_only, LOGGER


resource_path = Path(__file__).parent / 'resources'

    
def test_create_object(client):
    counter: int = 1
    LOGGER.info('Starting test_create_object')
    data = get_test_data('create_object.json')
    LOGGER.info('-- Got test data')
    LOGGER.info(f'-- Got {len(data["tasks"])} tasks')
    
    LOGGER.info('-- Starting loop\n')
    for obj in data['tasks']:
        LOGGER.info(f'-- -- Starting loop {counter}')
        LOGGER.info(f'-- -- Posting {obj["object"]} to {obj["path"]}')
        response = client.post(
            obj['path'],
            json=obj['object']
        )
        LOGGER.info(f'-- -- Got response {response}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f'-- -- Answer is {answer}')
        assert answer
        
        if response.status_code == HTTPStatus.CREATED:
            LOGGER.info(f'-- -- -- Comparing {response.json} to {obj["object"]}')
            answer = equal_dicts_only(response.json, obj['object'], 'type', 'created_by')
            LOGGER.info(f'-- -- -- Answer is {answer}')
            assert answer
            
            if 'data' in obj['object']:
                LOGGER.info(f'-- -- -- -- Comparing {response.json} to {obj["object"]}')
                answer = equal_dicts_exclude(response.json, obj['object'], '_id')
                LOGGER.info(f'-- -- -- -- Answer is {answer}')
                assert answer
        LOGGER.info(f'-- -- Loop {counter} done\n')
        counter += 1
    LOGGER.info('Done test_create_object\n\n')
            
    
def test_get_object(client):
    data = get_test_data('get_object.json')
    
    for obj in data['tasks']:
        response = client.post(
            obj['path'],
            json=obj['object']
        )
        assert response.status_code == HTTPStatus.CREATED

        id: str = response.json['_id']
        if not obj['valid']:
            id = obj['id']
        
        path = f'{obj["path"]}/{id}'
        response = client.get(
            path
        )
        assert response.status_code == obj['status_code']
        if not obj['valid']:
            continue
        
        assert equal_dicts_only(response.json, obj['object'], 'type')
        
        if 'data' in obj['object']:
            assert equal_dicts_only(response.json, obj['object'], 'type', 'data')
            
def test_update_object(client):
    data = get_test_data('update_object.json')
    
    for obj in data['tasks']:
        # Post object
        response = client.post(
            obj['path'],
            json=obj['old_object']
        )
        assert response.status_code == HTTPStatus.CREATED 
        
        # Put object
        path = f'{obj["path"]}/{response.json["_id"]}'
        response = client.put(
            path,
            json=obj['changes']
        )
        
        if response.status_code != HTTPStatus.NO_CONTENT:
            continue

        assert response.status_code == obj['status_code']
        
        # Get Updated object
        response = client.get(
            path
        )
        
        assert response.status_code == HTTPStatus.OK
        assert equal_dicts_exclude(response.json, obj['new_object'], '_id')
        
