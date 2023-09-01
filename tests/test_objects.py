from pathlib import Path

resource_path = Path(__file__).parent / 'resources'

def test_create_object(client):
    response = client.post(
        '/wastewise/objects',
        json={
            "type":"image",
            "created_by":"daniel"
        }
    )
    assert response.status_code == 201