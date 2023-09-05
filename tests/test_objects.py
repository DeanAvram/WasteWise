from pathlib import Path
from http import HTTPStatus
from tests.conftest import get_test_data, equal_dicts_exclude, equal_dicts_only


resource_path = Path(__file__).parent / 'resources'

    
def test_create_object(client):
    data = get_test_data('create_object.json')
    
    
    for obj in data['tasks']:
        response = client.post(
            obj['path'],
            json=obj['object']
        )
        
        assert response.status_code == obj['status_code']
        
        if response.status_code == HTTPStatus.CREATED:
            assert equal_dicts_only(response.json, obj['object'], 'type', 'created_by')
            
            if 'data' in obj['object']:
                assert equal_dicts_exclude(response.json, obj['object'], '_id')
    
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
        
