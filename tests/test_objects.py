from pathlib import Path
from http import HTTPStatus

resource_path = Path(__file__).parent / 'resources'

def test_create_object(client):
    response = client.post(
        '/wastewise/objects',
        json={
            "type":"image",
            "created_by":"daniel"
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json['type'] == 'image'
    assert response.json['created_by'] == 'daniel'
    
