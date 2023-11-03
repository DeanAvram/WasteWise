from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService, LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_get_all_users_1(client):
    admin = create_admin_user()
    user = create_user()

    response = client.get(
        f'/wastewise/admin/users?email={admin["email"]}&password={admin["password"]}'
    )
    
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 2
    
    response = client.delete(
        f'/wastewise/admin/users?email={admin["email"]}&password={admin["password"]}'
    )
    
    admin = create_admin_user()
    
    response = client.get(
        f'/wastewise/admin/users?email={admin["email"]}&password={admin["password"]}'
    )
    
    assert len(response.json) == 1
    