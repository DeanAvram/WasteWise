from http import HTTPStatus
from pathlib import Path

from tests.conftest import LOGGER, create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'


def test_get_all_users_1(client):
    LOGGER.info('Test get all users 1')
    LOGGER.info('1 user and 1 admin')
    admin = create_admin_user()
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    
    response = client.get(
        f'/wastewise/admin/users?email={admin["email"]}&password={admin["password"]}'
    )
    
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 2
    LOGGER.info('Test passed\n')


def test_get_all_users_2(client):
    LOGGER.info('Test get all users 2')
    admin = create_admin_user()
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

    response = client.get(
        f'/wastewise/admin/users?email={user["email"]}&password={user["password"]}'
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    
    LOGGER.info('Test passed\n')

    
