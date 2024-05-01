from http import HTTPStatus
from pathlib import Path

from fontTools.designspaceLib.split import LOGGER

from tests.conftest import create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'


def test_create_object_1(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            "type": "IMAGE",
            "data": {
                "url": "https://www.google.com"
            }
        }
    )
    LOGGER.error(response.response)
    assert response.status_code == HTTPStatus.CREATED


def test_create_object_2(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            "type": "IMAGE",
            "data": {
            }
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_object_3(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            "type": "IMAGE",
            "data": None
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_object_4(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            "type": "IMAGE",
        }
    )
    assert response.status_code == HTTPStatus.CREATED


def test_create_object_5(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            "type": "IMAGE",
        }
    )
    assert response.status_code == HTTPStatus.CREATED


def test_create_object_6(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
        }
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_object_7(client):
    """
    Create an object:
    Valid: no
    Explain: Invalid type of object
    """

    # create user
    user = create_user()

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            'type': 'BDHBDIBDI'
        }
    )
    LOGGER.info(response.json)
    assert response.status_code == HTTPStatus.BAD_REQUEST
