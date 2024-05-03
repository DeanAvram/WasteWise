from http import HTTPStatus
from pathlib import Path

from tests.conftest import LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_create_user_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for create user\n")

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
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: missing password")
    user = {
            "name": "test",
            "email": "test@gmail.com",
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

def test_create_user_5(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: missing role")
    user = {
            "name": "test",
            "email": "test@gmail.com",
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

def test_create_user_6(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: empty name")
    user = {
            "name": "",
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

def test_create_user_7(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: empty email")
    user = {
            "name": "test",
            "email": "",
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

def test_create_user_8(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: empty password")
    user = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "",
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

def test_create_user_9(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: empty role")
    user = {
            "name": "test",
            "email": "test@gmail.com",
            "password": "Testing193!",
            "role": ""
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


def test_create_user_10(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: 2 users with the same name")
    LOGGER.info("Expected: 201")
    user1 = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User1: {user1}")
    client.post(
        '/wastewise/users',
        json=user1
    )
    user2 = {
        "name": "test",
        "email": "test1@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User2: {user2}")
    response = client.post(
        '/wastewise/users',
        json=user2
    )
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info(f"Response answer: {answer}")
    assert answer
    LOGGER.info("Test create user finished\n")


def test_create_user_11(client):
    """
    Create a user:
    Valid: no
    Problem: email already exists
    """
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: email already exists")
    LOGGER.info("Expected: 400")

    user1 = {
        "name": "test1",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User1: {user1}")
    response = client.post(
        '/wastewise/users',
        json=user1
    )
    user2 = {
        "name": "test2",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"User2: {user2}")
    response = client.post(
        '/wastewise/users',
        json=user2
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Response answer: {answer}")
    assert answer
    LOGGER.info("Test create user finished\n")


def test_create_user_12(client):
    """
    Create a user:
    Valid: no
    Problem: wrong role
    """
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: wrong role")
    LOGGER.info("Expected: 400")

    user = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "not a valid role"
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

def test_create_user_13(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: password too short")

    user = {
        "name": "test",
        "email": "test@gmail.com",
        "password": "R1$4",
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

def test_create_user_14(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: password too long")

    user = {
            "name": "test",
            "email": "test@gmail.com",
            "password": "fSdfsderes@$#@$T",
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

def test_create_user_15(client):
    LOGGER.info("Test create user started")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: password no uppercase")

    user = {
            "name": "test",
            "email": "test@gmail.com",
            "password": "abcdefg123!",
            "role": "USER"
        }

    LOGGER.info(f"User: {user}")
    response = client.post(
        '/wastewise/users',
        json=user
    )

    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Response answer: {answer} \n\t, {response.json} ")
    assert answer
    LOGGER.info("Test create user finished\n")
