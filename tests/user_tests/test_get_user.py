from http import HTTPStatus
from pathlib import Path
from tests.conftest import LOGGER, create_user, create_admin_user

resource_path = Path(__file__).parent / 'resources'

def test_get_user_0(client):
    LOGGER.info("\n\n")
    LOGGER.info("Tests for GET /wastewise/users/{email}?email={email}&password={password}")


def test_get_user_1(client):
    LOGGER.info("Test Get User 1")
    LOGGER.info("Valid: yes")

    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")
    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password={usr["password"]}'
    )

    answer = response.status_code == HTTPStatus.OK
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 1 passed\n")


def test_get_user_2(client):
    LOGGER.info("Test Get User 2")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: invalid email")
    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")
    false_email = "false_email@gmail.com"
    LOGGER.info(f"False email: {false_email}")
    response = client.get(
        f'/wastewise/users/{false_email}?email={false_email}&password={usr["password"]}'
    )

    answer = response.status_code == HTTPStatus.NOT_FOUND
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 2 passed\n")


def test_get_user_3(client):
    LOGGER.info("Test Get User 3")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: missing request variables")
    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")

    response = client.get(
        f'/wastewise/users?email={usr["email"]}'
    )

    answer = response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 3 passed\n")


def test_get_user_4(client):
    LOGGER.info("Test Get User 4")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: unauthorized user")
    LOGGER.info("Explanation: admin user cannot get another user's information")

    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")
    admin = create_admin_user()
    LOGGER.info(f"Admin: {admin}")

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={admin["email"]}&password={admin["password"]}'
    )

    answer = response.status_code == HTTPStatus.FORBIDDEN
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 4 passed\n")


def test_get_user_5(client):
    LOGGER.info("Test Get User 5")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: wrong request password")
    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}'
    )

    answer = response.status_code == HTTPStatus.BAD_REQUEST
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 5 passed\n")

def test_get_user_6(client):
    LOGGER.info("Test Get User 6")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: invalid password")

    usr = create_user("User", "user@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User: {usr}")

    response = client.get(
        f'/wastewise/users/{usr["email"]}?email={usr["email"]}&password=invalid_password'
    )

    answer = response.status_code == HTTPStatus.UNAUTHORIZED
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 6 passed\n")

def test_get_user_7(client):
    LOGGER.info("Test Get User 7")
    LOGGER.info("Valid: no")
    LOGGER.info("Problem: user1 cannot get user2's information")

    usr1 = create_user("User1", "user1@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User1: {usr1}")
    usr2 = create_user("User2", "user2@gmail.com", "Testing193!", "USER")
    LOGGER.info(f"User2: {usr2}")

    response = client.get(
        f'/wastewise/users/{usr2["email"]}?email={usr1["email"]}&password={usr1["password"]}'
    )

    answer = response.status_code == HTTPStatus.FORBIDDEN
    LOGGER.info(f"answer: {answer}")
    LOGGER.info(f"Response: {response.json}")
    assert answer
    LOGGER.info("Test Get User 7 passed\n")
