from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService, LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_create_command_1(client):
    """Create general command test
    Valid: no
    Explain: Invalid type
    """
    
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    
    response = client.post(
        path,
        json={
                "type": "????",
                "data": {
                }
            }
    )
    
    LOGGER.info(response.json)
    
    assert response.status_code == HTTPStatus.BAD_REQUEST
    

def test_create_command_2(client):
    """Create general command test
    Valid: no
    Explain: ...
    """
    
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    
    response = client.post(
        path,
        json={
                "type": "GENERAL",
                "data": {
                }
            }
    )
    
    LOGGER.info(response.json)
    assert response.status_code == HTTPStatus.OK
    
    