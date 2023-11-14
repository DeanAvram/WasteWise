from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService
from passlib.hash import pbkdf2_sha256


resource_path = Path(__file__).parent / 'resources'


def test_update_user_1(client):

    """
    Update a user:
    Valid: yes
    Explain: password is valid to change
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        'password': 'Testing192!'
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.NO_CONTENT

    # check if data updated
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={data["password"]}',
    )
    assert response.status_code == HTTPStatus.OK
    assert pbkdf2_sha256.verify(data['password'], response.json['password'])


def test_update_user_2(client):
    """
    Update a user:
    Valid: yes
    Explain: role is valid to change
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        "role": "USER"
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.NO_CONTENT

    # check if data updated
    response = client.get(
         f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}'
    )
    assert equal_dicts_only(response.json, data, 'role')


def test_update_user_3(client):
    """
    Update a user:
    Valid: yes
    Explain: role is not valid to change
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        "role": "ADMIN"
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.BAD_REQUEST

    # check if data updated
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )
    assert not equal_dicts_only(response.json, data, 'role')


def test_update_user_4(client):
    """
    Update a user:
    Valid: yes
    Explain: role is not exists
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        "role": "NOT_VALID_ROLE"
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.BAD_REQUEST

    # check if data updated
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )
    assert not equal_dicts_only(response.json, data, 'role')


def test_update_user_5(client):
    """
    Update a user:
    Valid: yes
    Explain: change username
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        "name": "Name"
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.NO_CONTENT

    # check if data updated
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
    )

    assert equal_dicts_only(response.json, data, 'name')


def test_update_user_6(client):
    """
    Update a user:
    Valid: yes
    Explain: username is empty
    """

    # create
    usr = {
        "name": "User",
        "email": "user@gmail.com",
        "password": "Testing193!",
        "role": "USER"
    }
    userService.create_user(user=usr)
    # update

    data = {
        "name": ""
    }
    response = client.put(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}',
        json=data
    )
    # check if status is ok
    assert response.status_code == HTTPStatus.BAD_REQUEST

