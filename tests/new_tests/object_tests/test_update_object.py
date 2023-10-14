from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, objectService, equal_dicts_exclude, equal_dicts_only, LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_update_object_1(client):
    """
    Update an object:
    Valid: yes
    Explain:
    """
    # create user
    user: dict = create_user()

    # create object
    obj: dict = dict(type="image", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "data": {
            "url": "new"
        }
    }
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}',
        json=update
    )

    assert response_put.status_code == HTTPStatus.NO_CONTENT

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )

    assert not equal_dicts_only(response_get.json, response_post.json, 'data')


def test_update_object_2(client):
    """
    Update an object:
    Valid: No
    Explain: change type
    """
    user: dict = create_user()

    # create object
    obj: dict = dict(type="image", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "type":'NOT_OBJECT'
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
    user: dict = create_user()

    # create object
    obj: dict = dict(type="image", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "active": False
    }
    response_put = client.put(
        f'/wastewise/objects/{_id}?email={user["email"]}',
        json=update
    )

    assert response_put.status_code == HTTPStatus.NO_CONTENT

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )

    assert not equal_dicts_only(response_get.json, response_post.json, 'active')


def test_update_object_4(client):
    """
    Update an object:
    Valid: No
    Explain: change active to not valid
    """
    user: dict = create_user()

    # create object
    obj: dict = dict(type="image", data={
        "url": "https://www.google.com"
    })
    response_post = client.post(
        f'/wastewise/objects?email={user["email"]}',
        json=obj
    )

    _id: str = response_post.json['_id']

    # get
    response_get = client.get(
        f'/wastewise/objects/{_id}?email={user["email"]}'
    )
    # validate
    assert response_get.status_code == HTTPStatus.OK

    # update
    update: dict = {
        "active": 3
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