from http import HTTPStatus
from pathlib import Path

from tests.conftest import create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'


def test_get_all_users_1(client):
    """Get all user test
        Valid: yes
        Explain: valid GET request
    """
    admin = create_admin_user()
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    
    response = client.get(
        f'/wastewise/admin/users?email={admin["email"]}&password={admin["password"]}'
    )
    
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 2


def test_get_all_users_2(client):
    """Get all user test
        Valid: no
        Explain: USER try to get all users
    """
    admin = create_admin_user()
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")

    response = client.get(
        f'/wastewise/admin/users?email={user["email"]}&password={user["password"]}'
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    

    
