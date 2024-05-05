from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, create_user, create_object

resource_path = Path(__file__).parent / 'resources'


def test_get_object_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for GET /wastewise/objects\n")

def test_get_object_1(client):
    LOGGER.info("Test 1: Get an object")
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
    
    object = create_object(user, object)
    LOGGER.info("Object created") if object else LOGGER.error("Object not created")


    _id: str = object["_id"]

    LOGGER.info("Get object")
    response = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    LOGGER.info("Object got") if response else LOGGER.error("Object not got")
    LOGGER.info(response.json)
    LOGGER.info(response.status_code)
    # validate
    assert response.status_code == HTTPStatus.OK
    LOGGER.info("Test 1 passed\n")


def test_get_object_2(client):
    LOGGER.info("Test 2: Get an object")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: not found object")

    # create user
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

    # create object
    object = {
        "type": "IMAGE",
        "data": {
            "url": "https://www.google.com"
        }
    }    
    object = create_object(user, object)
    LOGGER.info("Object created") if object else LOGGER.error("Object not created")

    _id = "60e4c2f9e2d5f8b1c3d0e4e3"
    
    # get
    response = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    
    LOGGER.info(response.json)
    LOGGER.info(response.status_code)

    # validate
    assert response.status_code == HTTPStatus.NOT_FOUND
    LOGGER.info("Test 2 passed\n")
