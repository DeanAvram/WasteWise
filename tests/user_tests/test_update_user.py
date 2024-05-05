from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService
from passlib.hash import pbkdf2_sha256


resource_path = Path(__file__).parent / 'resources'

def test_update_user_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for PUT /wastewise/users/{email}?email={email}&password={password}\n")

def test_update_user_1(client):
    LOGGER.info("Test Update User 1")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: Update password")

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        'password': 'Testing192!'
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    answer = response.status_code == HTTPStatus.NO_CONTENT
    LOGGER.info(f"Response: {response.json}")
    assert answer

    # check if data updated
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={data["password"]}',
    )
    answer = response.status_code == HTTPStatus.OK
    assert answer
    LOGGER.info(f"Response: {response.json}")

    answer = pbkdf2_sha256.verify(data['password'], response.json['password'])
    LOGGER.info(f"Password is correct: {answer}")
    assert answer
    LOGGER.info("Test Update User 1 Passed\n")


def test_update_user_2(client):
    LOGGER.info("Test Update User 2")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: role is valid to change")
    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "role": "USER"
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    answer = response.status_code == HTTPStatus.NO_CONTENT
    LOGGER.info(f"Response: {response.json}")
    assert answer

    response = client.get(
         f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}'
    )
    answer = response.status_code == HTTPStatus.OK
    LOGGER.info(f"Response: {response.json}")
    assert answer
    answer = equal_dicts_only(response.json, data, 'role')
    LOGGER.info(f"Role is correct: {answer}")
    assert answer
    LOGGER.info("Test Update User 2 Passed\n")


def test_update_user_3(client):
    LOGGER.info("Test Update User 3")
    LOGGER.info("Valid: No")
    LOGGER.info("Explain: role is not valid to change")

    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)
    data = {
        "role": "ADMIN"
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )
    answer = response.status_code == HTTPStatus.OK
    LOGGER.info(f"Response: {response.json}")
    assert answer
    answer = not equal_dicts_only(response.json, data, 'role')
    LOGGER.info(f"Role is correct: {answer}")
    assert answer

    answer = response.json['role'] == usr['role']
    LOGGER.info(f"Role is correct: {answer}")
    assert answer

    LOGGER.info("Test Update User 3 Passed\n")


def test_update_user_4(client):
    LOGGER.info("Test Update User 4")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: role is not valid")
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)
    LOGGER.info(f"User created")
    data = {
        "role": "NOT_VALID_ROLE"
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )
    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = response.json['role'] == usr['role']
    LOGGER.info(f"Role is correct: {answer}")
    assert answer
    LOGGER.info("Test Update User 4 Passed\n")

def test_update_user_5(client):
    LOGGER.info("Test Update User 5")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: change username")
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "name": "Name"
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.NO_CONTENT
    assert answer

    LOGGER.info("Getting user")
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )
    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = equal_dicts_only(response.json, data, 'name')
    LOGGER.info(f"Name is correct: {answer}")
    assert answer
    LOGGER.info("Test Update User 5 Passed\n")


def test_update_user_6(client):
    LOGGER.info("Test Update User 6")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: username is empty")
    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "name": ""
    }
    LOGGER.info(f"Updating user with data: {data}")
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}')

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = not equal_dicts_only(response.json, data, 'name')
    LOGGER.info("Test Update User 6 Passed\n")

def test_update_user_7(client):
    LOGGER.info("Test Update User 7")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: password is too short")

    usr = {
        "name": "User",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }

    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "password": "Test1!"
    }

    LOGGER.info(f"Updating user with data: {data}")

    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}')

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = response.json['password'] == usr['password']
    LOGGER.info("Test Update User 7 Passed\n")

def test_update_user_8(client):
    LOGGER.info("Test Update User 8")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: update to the same password")

    usr = {
        "name": "User",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }

    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "password": "Testing193!"
    }

    LOGGER.info(f"Updating user with data: {data}")

    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}')

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = response.json['password'] == usr['password']
    LOGGER.info("Test Update User 8 Passed\n")

def test_update_user_9(client):
    LOGGER.info("Test Update User 9")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: password is too long")

    usr = {
        "name": "User",
        "email": "test@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }

    LOGGER.info(f"Creating user: {usr}")
    userService.create_user(user=usr)

    data = {
        "password": "Test1!aaaaaaaaaaaaaaaaaa"
    }

    LOGGER.info(f"Updating user with data: {data}")

    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"Answer: {answer}")
    assert answer

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}')

    LOGGER.info(f"Response: {response.json}")
    answer = response.status_code == HTTPStatus.OK
    assert answer
    answer = response.json['password'] == usr['password']
    LOGGER.info("Test Update User 9 Passed\n")
