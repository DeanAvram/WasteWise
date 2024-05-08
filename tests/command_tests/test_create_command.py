from http import HTTPStatus
from pathlib import Path
from tests.conftest import create_user, create_admin_user, create_object
from tests.conftest import userService, LOGGER

resource_path = Path(__file__).parent / 'resources'


def test_create_command_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for POST /wastewise/commands\n")


def test_create_command_1(client):
    LOGGER.info("Test create command 1")
    LOGGER.info("Valid: no")
    LOGGER.info("Explain: Unknown command type")

    LOGGER.info("Creating user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")

    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")
    command_type = "????"
    LOGGER.info(f"Command type: {command_type}")
    command = {
        "type": command_type,
        "data": {
        }
    }
    LOGGER.info(f"Command: {command}")
    response = client.post(
        path,
        json=command
    )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info("Test passed\n")


def test_create_command_2(client):
    LOGGER.info("Test create command 2")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: General command")

    LOGGER.info("Creating user")
    user = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")

    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")

    command_type = "GENERAL"
    LOGGER.info(f"Command type: {command_type}")

    command = {
        "type": command_type,
        "data": {
        }
    }
    LOGGER.info(f"Command: {command}")

    LOGGER.info("Sending request")
    response = client.post(
        path,
        json=command
    )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED

    LOGGER.info(f'Test passed\n')


def test_create_command_3(client):
    LOGGER.info("Test create command 3")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: Direct command")

    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")

    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")
    
    LOGGER.info("Creating admin user")
    admin = create_admin_user()
    LOGGER.info("Admin user created")
    
    LOGGER.info("Creating object")
    object = {
        "type": "PUBLIC_FACILITY",
        "data": {
            "name": "Recycle Facility",
            "bin_type": "paper",
            "location": {
                "coordinates": [
                    34.752834537498536,
                    32.03852621707681
                ]
            }
        }
    }
    
    object = create_object(admin, object)
    LOGGER.info("Object created")

    command_type = "DIRECT"
    LOGGER.info(f"Command type: {command_type}")

    command = {
        "type": command_type,
        "data": {
            'bin_type': "paper",
            'location': {
                'lng': 0.0,
                'lat': 0.0
            }
        }
    }
    LOGGER.info(f"Command: {command}")

    LOGGER.info("Sending request")
    response = client.post(
        path,
        json=command
    )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')

    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info(f'Test passed\n')
