from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'


def test_get_user_1(client):
    """
    Get a user:
    Valid: yes
    """

    usr = create_user()
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}'
    )

    assert response.status_code == HTTPStatus.OK


def test_get_user_2(client):
    """
    Get a user:
    Valid: no
    Problem: missing email
    """
    usr = create_user()

    response = client.get(
        f'/wastewise/users/{usr["email"]}'
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_user_3(client):
    """
    Get a user:
    Valid: no
    Problem: missing email
    """
    usr = create_user()

    response = client.get(
        f'/wastewise/users?email={usr["email"]}'
    )

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_get_user_4(client):
    """
    Get a user:
    Valid: no
    Problem: unauthorized email
    """

    usr = create_user()
    admin = create_admin_user()

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={admin["email"]}'
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED

