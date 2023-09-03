from pathlib import Path
from http import HTTPStatus

from tests.conftest import get_test_data


resource_path = Path(__file__).parent / 'resources'

    



def test_create_object(client):
    data = get_test_data('create_object.json')
    for obj in data['data']:
        response = client.post(
            obj['path'],
            json=obj['object']
        )
        assert response.status_code == obj['status_code']
        assert response.json['type'] == obj['object']['type']
        assert response.json['created_by'] == obj['object']['created_by']
    
