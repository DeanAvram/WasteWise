from pathlib import Path
from http import HTTPStatus

from tests.conftest import get_test_data


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
            assert response.json['type'] == obj['object']['type']
            assert response.json['created_by'] == obj['object']['created_by']
            
            if 'data' in obj['object']:
                assert response.json['data'] == obj['object']['data']
    
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
        assert response.json['type'] == obj['object']['type']
        
        if 'data' in obj['object']:
            assert response.json['data'] == obj['object']['data']
            
def test_update_object(client):
    ...