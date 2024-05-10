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

def test_create_command_4(client):
    LOGGER.info("Test create command 4")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: Direct command, with 2 location")

    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")

    LOGGER.info("Creating admin user")
    admin = create_admin_user()

    LOGGER.info("Creating object")
    object1 = {
        "type": "PUBLIC_FACILITY",
        "data": {
            "name": "Recycle Facility 1",
            "bin_type": "paper",
            "location": {
                "coordinates": [
                   31.5516,34.6742
                ]
            }
        }
    }
    object = create_object(admin, object1)

    object2 = {
        "type": "PUBLIC_FACILITY",
        "data": {
            "name": "Recycle Facility 2",
            "bin_type": "paper",
            "location": {
                "coordinates": [
                   31.89549,35.00969
                ]
            }
        }
    }
    object = create_object(admin, object2)

    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")

    command_type = "DIRECT"
    LOGGER.info(f"Command type: {command_type}")

    command = {
        "type": command_type,
        "data": {
            'bin_type': "paper",
            'location': {
                'lng': 31.89527,
                'lat': 35.01055
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
    
def test_create_command_5(client):
    LOGGER.info("Test create command 5")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: Direct command, with 0 location")

    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
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
    assert response.status_code == HTTPStatus.NOT_FOUND
    LOGGER.info(f'Test passed\n')
    
def test_create_command_6(client):
    LOGGER.info("Test create command 6")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: History command of 1 command")
    
    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")
    
    LOGGER.info("Add Classifications")
    
    image = open('tests/test_data/images/glass.jpg', 'rb')
    assert image is not None
    LOGGER.info("Image opened")
    
    path = f'/wastewise/classify?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
    LOGGER.info("Sending request")
    response = client.post(
            path,
            data=image,
            content_type='image/jpeg'
        )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info("Classification is glass") if response.json['classification'] == 'glass' else LOGGER.error("Classification is not glass")
    
    LOGGER.info(f'Create History Command')
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'

    command_type = 'HISTORY'

    command = {
        "type": command_type,
        "data": {
            "period": "WEEK"
        }
    }
    LOGGER.info(f'Command = {command}')

    response = client.post(
        path,
        json=command
    )

    LOGGER.info(f'Respone = {response.json}')
    LOGGER.info(f'Status code = {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info('Test passed\n')

def test_create_command_7(client):
    LOGGER.info("Test create command 7")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: History command of 2 commands")
    
    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")
    
    LOGGER.info("Add Classification 1")
    
    image = open('tests/test_data/images/glass.jpg', 'rb')
    assert image is not None
    LOGGER.info("Image opened")
    
    path = f'/wastewise/classify?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
    LOGGER.info("Sending request")
    response = client.post(
            path,
            data=image,
            content_type='image/jpeg'
        )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info("Classification is glass") if response.json['classification'] == 'glass' else LOGGER.error("Classification is not glass")
    
    LOGGER.info("Add Classification 2")
    image = open('tests/test_data/images/plastic.jpeg', 'rb')
    assert image is not None
    LOGGER.info("Image opened")

    path = f'/wastewise/classify?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")    
    
    LOGGER.info("Sending request")
    response = client.post(
            path,
            data=image,
            content_type='image/jpeg'
        )
    LOGGER.info(f'Response: {response.json}')
    LOGGER.info(f'Status code: {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info("Classification is plastic") if response.json['classification'] == 'plastic' else LOGGER.error("Classification is not glass")
    

    LOGGER.info(f'Create History Command')
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'

    command_type = 'HISTORY'

    command = {
        "type": command_type,
        "data": {
            "period": "WEEK"
        }
    }
    LOGGER.info(f'Command = {command}')

    response = client.post(
        path,
        json=command
    )

    LOGGER.info(f'Respone = {response.json}')
    LOGGER.info(f'Status code = {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    assert len(response.json) == 2
    LOGGER.info('Test passed\n')
    
def test_create_command_8(client):
    LOGGER.info("Test create command 8")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: History command of 0 commands")

    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")

    LOGGER.info(f'Create History Command')
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'

    command_type = 'HISTORY'

    command = {
        "type": command_type,
        "data": {
            "period": "WEEK"
        }
    }
    LOGGER.info(f'Command = {command}')

    response = client.post(
        path,
        json=command
    )

    LOGGER.info(f'Respone = {response.json}')
    LOGGER.info(f'Status code = {response.status_code}')
    assert response.status_code == HTTPStatus.CREATED
    LOGGER.info('Test passed\n')

def test_create_command_9(client):
    LOGGER.info("Test create command 8")
    LOGGER.info("Valid: yes")
    LOGGER.info("Explain: Get Places")

    LOGGER.info("Creating user")
    user: dict = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info("User created")
    
    LOGGER.info("Create Admin")
    admin = create_admin_user()
    LOGGER.info('Admin Created')

    LOGGER.info('Create Recycle Facilites')

    LOGGER.info("Creating object 1")
    object1 = {
        "type": "PUBLIC_FACILITY",
        "data": {
            "name": "Recycle Facility 1",
            "bin_type": "paper",
            "location": {
                "coordinates": [
                   31.5516,34.6742
                ]
            }
        }
    }
    object = create_object(admin, object1)
    LOGGER.info(f'Object {object}')

    LOGGER.info("Creating object 2")
    object2 = {
        "type": "PUBLIC_FACILITY",
        "data": {
            "name": "Recycle Facility 2",
            "bin_type": "paper",
            "location": {
                "coordinates": [
                   31.89549,35.00969
                ]
            }
        }
    }
    object = create_object(admin, object2) 
    LOGGER.info(f'Object {object}')

    LOGGER.info('Create Command')
    path = f'/wastewise/commands?email={user["email"]}&password={user["password"]}'
    LOGGER.info(f"Path: {path}")

    command_type = "FACILITIES"
    LOGGER.info(f"Command type: {command_type}")

    command = {
        "type": command_type,
        "data": {
            "location": {
                "lng": 31.89521,
                "lat":35.00946 
            },
            "radius":1000000000000000
        }
    }
    LOGGER.info(f'Command: {command}')
    
    response = client.post(
        path,
        json=command
    )

    LOGGER.info(f'Response: {response.json}')

    LOGGER.info(f'Http Status: {response.status_code}')



     
