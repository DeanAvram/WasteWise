from http import HTTPStatus
from pathlib import Path
from tests.conftest import get_test_data, LOGGER, equal_dicts_exclude

resource_path = Path(__file__).parent / 'resources'


def test_create_user(client):
    counter: int = 1
    success: int = 0

    LOGGER.info(' Starting: test_create_user')
    data = get_test_data('create_user.json')
    length: int = len(data['tasks'])
    LOGGER.info(f' Got {length} tasks')

    LOGGER.info('')
    for usr in data['tasks']:
        LOGGER.info(f' ##### TITLE : {usr["title"]} #####')
        LOGGER.info(f' 1) Starting create user Test {counter}')
        try:
            LOGGER.info(f' 2) Posting {usr["user"]} to {usr["path"]}')
            response = client.post(
                usr['path'],
                json=usr['user']
            )
        except Exception as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 3) Got response {response}')
        LOGGER.info(f' 4) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f' 5) comparison is {answer}')
        try:
            assert answer
        except AssertionError as e:
            LOGGER.error(f' Failing test {counter}')
            LOGGER.error(f' Got exception {e}')
            counter += 1
            continue

        if response.status_code == HTTPStatus.CREATED:
            LOGGER.info(f' 6) Comparing {response.json} to {usr["user"]}')
            answer = equal_dicts_exclude(response.json, usr['user'], '_id')
            LOGGER.info(f' 7) comparison is {answer}')
            try:
                assert answer
            except AssertionError as e:
                LOGGER.error(f' Got exception {e}')
                LOGGER.error(f' Failing test {counter}')
                counter += 1
                continue

        LOGGER.info(f' succeeded {counter} of {length}')
        success += 1
        counter += 1

    LOGGER.info(f' Succeeded: {success} of {length}')


def test_get_user(client):
    counter: int = 1
    success: int = 0
    LOGGER.info(' Starting: test_get_user')
    data = get_test_data('get_user.json')
    LOGGER.info(' Got test data')
    length: int = len(data['tasks'])
    LOGGER.info(f' Got {length} tasks')

    LOGGER.info('')
    for usr in data['tasks']:
        LOGGER.info(f' ##### TITLE : {usr["title"]} #####')
        LOGGER.info(f' 1) Starting get user Test {counter}')
        LOGGER.info(f' 2) Posting {usr["user"]} to {usr["path"]}')
        try:
            response = client.post(
                usr['path'],
                json=usr['user']
            )
        except Exception as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 3) Got response {response}')
        # get user
        LOGGER.info(f' 4) Getting user {usr["user"]["email"]}')
        path: str = usr['path'] + '/' + usr['user']['email']
        try:
            response = client.get(
                f'{path}?email=user@gmail.com'
            )
        except Exception as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 5) Got response {response}')
        LOGGER.info(f'6) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f' 7) comparison is {answer}')
        try:
            assert answer
        except AssertionError as e:
            LOGGER.error(f' Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' succeeded {counter} of {length}')

        counter += 1
        success += 1
    LOGGER.info(f' Succeeded: {success} of {length} ')


def test_update_user(client):
    counter: int = 1
    success: int = 0

    LOGGER.info(' Starting: test_update_user')
    data = get_test_data('update_user.json')
    LOGGER.info(' Got test data')
    length: int = len(data['tasks'])
    LOGGER.info(f' Got {length} tasks')

    LOGGER.info('3) Starting loop')
    for usr in data['tasks']:
        LOGGER.info(f' ##### TITLE : {usr["title"]} #####')
        LOGGER.info(f' 1) Starting update user Test {counter}')
        LOGGER.info(f' 2) Posting {usr["old_user"]} to {usr["path"]}')
        try:
            response = client.post(
                usr['path'],
                json=usr['old_user']
            )
        except Exception as e:
            LOGGER.error(f'Got exception {e}')
            LOGGER.error(f'Failing test {counter}')
            counter += 1
            continue
        LOGGER.info(f' 3) Got response {response}')

        # update user
        LOGGER.info(f' 4) Updating user {usr["old_user"]["email"]}')
        path: str = usr['path'] + '/' + usr['old_user']['email']
        try:
            response = client.put(
                f'{path}?email=user@gmail.com',
                json=usr['changes']
            )
        except Exception as e:
            LOGGER.error(f'Got exception {e}')
            LOGGER.error(f'Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 5) Got response {response}')
        LOGGER.info(f' 6) Got response {response.json}')
        answer = response.status_code == usr['status_code']
        LOGGER.info(f' 7) comparison is {answer} -> {response.status_code} == {usr["status_code"]}')
        try:
            assert answer
        except AssertionError as e:
            LOGGER.error(f'Got exception {e}')
            LOGGER.error(f'Failing test {counter}')
            counter += 1
            continue

        if response.status_code == HTTPStatus.NO_CONTENT:
            # get user
            LOGGER.info(f' 8) Getting user {usr["old_user"]["email"]}')
            path: str = usr['path'] + '/' + usr['old_user']['email']
            try:
                response = client.get(
                    f'{path}?email=user@gmail.com'
                )
            except Exception as e:
                LOGGER.error(f' Got exception {e}')
                LOGGER.error(f' Failing test {counter}')
                counter += 1
                continue

            LOGGER.info(f' 9) Comparing: \t{response.json} to \t{usr["new_user"]}')
            answer = equal_dicts_exclude(response.json, usr['new_user'], '_id')
            LOGGER.info(f' 10) comparison is {answer}')
            try:
                assert answer
            except AssertionError as e:
                LOGGER.error(f' Got exception {e}')
                LOGGER.error(f' Failing test {counter}')
                counter += 1
                continue

        LOGGER.info(f' succeeded {counter}')
        counter += 1
        success += 1
    LOGGER.info(f' Succeeded: {success} of {length} ')
