from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService

resource_path = Path(__file__).parent / 'resources'

def test_create_command_1(client):
    ...