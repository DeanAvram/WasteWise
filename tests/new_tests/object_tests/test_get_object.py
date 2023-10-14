from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, objectService

resource_path = Path(__file__).parent / 'resources'


def test_get_object_1(client):
    """
    Create an object:
    Valid: yes
    Explain: get object
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}',
        json={
            "type": "image",
            "data": {
                "url": "https://www.google.com"
            }
        }
    )
    _id: str = response.json['_id']

    # get
    response = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )

    # validate
    assert response.status_code == HTTPStatus.OK


def test_get_object_2(client):
    """
    Create an object:
    Valid: yes
    Explain: get object
    """

    #