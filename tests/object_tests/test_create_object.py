from http import HTTPStatus
from pathlib import Path

from fontTools.designspaceLib.split import LOGGER

from tests.conftest import create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'


def test_create_object_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for POST /wastewise/objects\n")


def test_create_object_1(client):
    LOGGER.info("Test 1: Create an object")
    LOGGER.info("Valid: yes")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    object = {
        "type": "IMAGE",
        "data": {
            "url": "https://www.google.com"
        }
    }
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=object
    )
    LOGGER.info("Object created")
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info("Answer: %s", answer)
    LOGGER.info("Response: %s", response.json)
    assert answer
    LOGGER.info("Test 1 passed\n")


def test_create_object_2(client):
    LOGGER.info("Test 2: Create an object")
    LOGGER.info("Valid: no")
    LOGGER.info("IMAGE object without data")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    object = {
        "type": "IMAGE",
        "data": {
        }
    }
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=object
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Object not created") if answer else LOGGER.error("Object created")

    assert answer
    LOGGER.info("Test 2 passed\n")


def test_create_object_3(client):
    LOGGER.info("Test 3: Create an object")
    LOGGER.info("Valid: no")
    LOGGER.info("IMAGE object empty data")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    object = {
        "type": "IMAGE",
        "data": None
    }
    LOGGER.info("Object: %s", object)
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=object
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Object not created") if answer else LOGGER.error("Object created")
    LOGGER.info("Response: %s", response.json)

    assert answer
    LOGGER.info("Test 3 passed\n")


def test_create_object_4(client):
    LOGGER.info("Test 4: Create an object")
    LOGGER.info("Valid: no")
    LOGGER.info("IMAGE object without data")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    object = {
        "type": "IMAGE"
    }
    LOGGER.info("Object: %s", object)
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=object
    )
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info("Object created") if not answer else LOGGER.error("Object not created")
    assert answer
    LOGGER.info("Test 4 passed\n")


def test_create_object_5(client):
    LOGGER.info("Test 5: Create an object")
    LOGGER.info("Valid: no")
    LOGGER.info("Object without json")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
        }
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Object created") if not answer else LOGGER.error("Object not created")
    assert answer
    LOGGER.info("Test 5 passed\n")


def test_create_object_6(client):
    LOGGER.info("Test 6: Create an object")
    LOGGER.info("Valid: no")
    LOGGER.info("Object without type")

    LOGGER.info("Create a user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    object = {
        'type': 'BHFHFHFHF'
    }
    LOGGER.info("Object: %s", object)
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=object
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Object created") if not answer else LOGGER.error("Object not created")

    assert answer
    LOGGER.info("Test 6 passed\n")

