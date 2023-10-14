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
    objectService.create_object(
        user['email'],
        {
            "type": "IMAGE"
        }
    )


    # get
    response = client.get(
        f'/wastewise/objects/{user["email"]}?email={user["email"]}'
    )

    # validate
    assert response.status_code == HTTPStatus.OK

