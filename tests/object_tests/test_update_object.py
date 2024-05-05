from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, create_object, create_user, equal_dicts_only

resource_path = Path(__file__).parent / 'resources'

def test_update_object_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for GET /wastewise/objects\n")

def test_update_object_1(client):
    LOGGER.info("Test 1: Update an object")
    LOGGER.info("Valid: Yes")
    LOGGER.info("Explain: change data")
    
    
    LOGGER.info("Create a user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    obj = create_object(user, obj)
    LOGGER.info("Object created") if obj else LOGGER.error("Object not created")
    _id: str = obj["_id"]

    

    LOGGER.info("Update object") 
    update: dict = {
        "data": {
            "url": "new"
        }
    }
    LOGGER.info(f'Update: {update}')
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}',
        json=update
    )

    answer = response_put.status_code == HTTPStatus.NO_CONTENT
    LOGGER.info("Object updated") if answer else LOGGER.error("Object not updated")
    assert answer

    LOGGER.info("Get object after update")
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    assert response_get.status_code == HTTPStatus.OK
    answer = update['data'] == response_get.json['data']
    LOGGER.info("Object updated correctly") if answer else LOGGER.error("Object not updated correctly")
    LOGGER.info(f'Expected: {update["data"]}')
    LOGGER.info(f'Got: {response_get.json["data"]}')
    assert answer
    LOGGER.info("Test 1 passed\n")


def test_update_object_2(client):
    """
    Update an object:
    Valid: No
    Explain: change type
    """
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")

    # create object
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "type": 'NOT_OBJECT'
    }
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}',
        json=update
    )

    assert response_put.status_code == HTTPStatus.BAD_REQUEST

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )

    assert equal_dicts_only(response_get.json, response_post.json)


def test_update_object_3(client):
    """
    Update an object:
    Valid: Yes
    Explain: change active
    """
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")

    # create object
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=obj
    )
    _id: str = response_post.json['_id']
    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )

    # validate
    assert response_get.status_code == HTTPStatus.OK
    # update
    update: dict = {
        "active": False
    }
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}',
        json=update
    )
    assert response_put.status_code == HTTPStatus.NO_CONTENT
    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    assert not equal_dicts_only(response_get.json, response_post.json, 'active')


def test_update_object_4(client):
    """
    Update an object:
    Valid: No
    Explain: change active to not valid
    """
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")

    # create object
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}&password={user["password"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "active": 3
    }
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}',
        json=update
    )

    assert response_put.status_code == HTTPStatus.BAD_REQUEST

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )

    assert equal_dicts_only(response_get.json, response_post.json)
