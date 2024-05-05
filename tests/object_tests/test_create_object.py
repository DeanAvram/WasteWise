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
    LOGGER.info("Valid: yes")


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
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info("Object created") if answer else LOGGER.error("Object not created")


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
    answer = response.status_code == HTTPStatus.CREATED
    LOGGER.info("Object created") if answer else LOGGER.error("Object not created")


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
    LOGGER.info("Object created") if answer else LOGGER.error("Object not created")


def test_create_object_5(client):
    """
    Create an object:
    Valid: yes
    Explain: ...
    """

    # create user
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

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
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

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
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

    # create object
    response = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json={
            'type': 'BDHBDIBDI'
        }
    )
    LOGGER.info(response.json)
    assert response.status_code == HTTPStatus.BAD_REQUEST
