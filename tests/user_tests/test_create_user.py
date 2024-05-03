from http import HTTPStatus
from pathlib import Path

from tests.conftest import LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_create_user_1(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: yes")

    user = {"name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "USER"}
    LOGGER.info(f"User: {user}")
    response = client.post(
        '/wastewise/users',
        json=user
    )
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info(f"Response answer: {answer}")
    assert answer
    LOGGER.info("Test create user finished\n")


def test_create_user_2(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: missing name")
    user = {
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User: {user}")
    response = client.post(
        '/wastewise/users',
        json=user
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Response answer: {answer}")
    assert answer
    LOGGER.info("Test create user finished\n")


def test_create_user_3(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: missing password")
    user = {
        "name": "test",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User: {user}")
    response = client.post(
        '/wastewise/users',
        json=user
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Response answer: {answer}")
    assert answer
    LOGGER.info("Test create user finished\n")


def test_create_user_4(client):
    """
    Create a user:
    Valid: no
    Problem: missing password
    """
    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "role": "USER"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_5(client):
    """
    Create a user:
    Valid: no
    Problem: missing role
    """
    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "role": "USER"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_6(client):
    """
    Create a user:
    Valid: no
    Problem: empty name
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "USER"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_7(client):
    """
    Create a user:
    Valid: no
    Problem: empty email
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "",
            "password": "Testing193!",
            "role": "USER"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_8(client):
    """
    Create a user:
    Valid: no
    Problem: empty password
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "password": "",
            "role": "USER"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_9(client):
    """
    Create a user:
    Valid: no
    Problem: empty role
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": ""
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_10(client):
    """"
    Create a user:
    Valid: yes
    Problem:
    """

    client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "USER"
        }
    )

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test1@gmail.com",
            "password": "Testing193!",
            "role": "USER"
        }
    )
    # print(response.json)
    assert response.status_code == HTTPStatus.CREATED


def test_create_user_11(client):
    """
    Create a user:
    Valid: no
    Problem: email already exists
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "USER"
        }
    )
    LOGGER.info(response)

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test1",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "USER"
        }
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_12(client):
    """
    Create a user:
    Valid: no
    Problem: wrong role
    """

    response = client.post(
        '/wastewise/users',
        json={
            "name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": "not role"
        }
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
