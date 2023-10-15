from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, equal_dicts_only
from tests.conftest import userService, LOGGER

resource_path = Path(__file__).parent / 'resources'