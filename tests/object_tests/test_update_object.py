from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, create_object, create_user 

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
    LOGGER.info("Test 2: Update an object")
    LOGGER.info("Valid: No")
    LOGGER.info("Explain: change type to not valid")
    
    LOGGER.info("Create a user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")

    LOGGER.info("Create an object")
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    LOGGER.info(f'Object: {obj}')
    obj = create_object(user, obj)
    LOGGER.info("Object created") if obj else LOGGER.error("Object not created")

    _id: str = obj["_id"]

    LOGGER.info("Update object")
    update: dict = {
        "type": 'NOT_OBJECT'
    }
    LOGGER.info(f'Update: {update}')
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}',
        json=update
    )
    LOGGER.info(response_put.json)
    LOGGER.info(response_put.status_code)
    answer = response_put.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Object not updated") if answer else LOGGER.error("Object updated")
    assert answer

    LOGGER.info("Get object after update")
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )

    assert response_get.status_code == HTTPStatus.OK
    answer = response_get.json['type'] == obj['type']
    LOGGER.info("Object not updated correctly") if answer else LOGGER.error("Object updated correctly")
    LOGGER.info(f'Expected: {obj["type"]}')
    LOGGER.info(f'Got: {response_get.json["type"]}')
    assert answer
    LOGGER.info("Test 2 passed\n")

def test_update_object_3(client):
    LOGGER.info("Test 3: Update an object")
    LOGGER.info("Valid: Yes")
    LOGGER.info("Explain: change active")
    
    LOGGER.info("Create a user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")
    
    LOGGER.info("Create an object")
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    LOGGER.info(f'Object: {obj}')
    obj = create_object(user, obj)
    _id: str = obj['_id']
    
    

    LOGGER.info("Update object")
    update: dict = {
        "active": False
    }
    LOGGER.info(f'Update: {update}')
    
    LOGGER.info("Update object")
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}',
        json=update
    )
    answer = response_put.status_code == HTTPStatus.NO_CONTENT
    LOGGER.info("Object updated") if answer else LOGGER.error("Object not updated")
    
    LOGGER.info("Get object after update")
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    assert response_get.status_code == HTTPStatus.OK
    answer = response_get.json['active'] == update['active']
    LOGGER.info("Object updated correctly") if answer else LOGGER.error("Object not updated correctly")
    LOGGER.info(f'Expected: {update["active"]}')
    LOGGER.info(f'Got: {response_get.json["active"]}')
    assert answer
    LOGGER.info("Test 3 passed\n")


def test_update_object_4(client):
    LOGGER.info("Test 4: Update an object")
    LOGGER.info("Valid: No")
    LOGGER.info("Explain: change active by other user")
    
    LOGGER.info("Create a user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created") if user else LOGGER.error("User not created")
    
    LOGGER.info("Create an object")
    obj: dict = dict(type="IMAGE", data={
        "url": "https://www.google.com"
    })
    
    obj = create_object(user, obj)
    _id: str = obj['_id']
    
    LOGGER.info("Create another user")
    user2: dict = create_user("User2", "user2@gmail.com", "Testing193!", "USER")
    LOGGER.info("User2 created") if user2 else LOGGER.error("User2 not created")
    
    LOGGER.info("Update object")
    update: dict = {
        "active": False
    }
    
    LOGGER.info(f'Update: {update}')
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user2["email"]}&password={user2["password"]}',
        json=update
    )
    
    LOGGER.info(response_put.json)
    LOGGER.info(response_put.status_code)
    answer = response_put.status_code == HTTPStatus.FORBIDDEN
    
    LOGGER.info("Object not updated") if answer else LOGGER.error("Object updated")
    assert answer
    
    LOGGER.info("Get object after update")
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}&password={user["password"]}'
    )
    
    assert response_get.status_code == HTTPStatus.OK
    answer = response_get.json['active'] == obj['active']
    LOGGER.info("Object not updated correctly") if answer else LOGGER.error("Object updated correctly")
    LOGGER.info(f'Expected: {obj["active"]}')
    LOGGER.info(f'Got: {response_get.json["active"]}')
    assert answer
    LOGGER.info("Test 4 passed\n")