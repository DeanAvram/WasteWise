from pathlib import Path
from http import HTTPStatus
from tests.conftest import (get_test_data, equal_dicts_exclude, equal_dicts_only, LOGGER, next_sub_test, end_loop,
                            start_test)


resource_path = Path(__file__).parent / 'resources'




def test_create_object(client):
    counter: int = 1
    success: int = 0
    length: int = 0
    data: dict = {}

    data, length = start_test(data, length, 'create_object.json', 'test_create_object')
    for obj in data['tasks']:
        LOGGER.info(f' ##### TITLE : {obj["title"]} ####')
        LOGGER.info(f' 1) Posting \t{obj["object"]} \tto \t{obj["path"]}')
        path = obj['path']
        try:
            response = client.post(
                f'{path}?email=user@gmail.com',
                json=obj['object']
            )
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 2) Got response {response}')
        LOGGER.info(f' 3) Got response {response.json}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f' 4) comparison is {answer} : {response.status_code} =? {obj["status_code"]}')

        try:
            assert answer
        except AssertionError as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 5) Checking if test {counter} is valid')
        if response.status_code == HTTPStatus.CREATED:
            LOGGER.info(f' 6) Comparing :\t{response.json} \tto \t{obj["object"]}')
            answer = equal_dicts_only(response.json, obj['object'], 'type')
            LOGGER.info(f' 7) comparison is {answer}')

            try:
                assert answer
            except AssertionError as e:
                counter = next_sub_test(e, counter)
                continue

            LOGGER.info(f' 8) Checking if test {counter} has data')
            if 'data' in obj['object']:
                LOGGER.info(f' 9) Comparing {response.json} to {obj["object"]}')
                answer = equal_dicts_exclude(response.json, obj['object'], '_id', 'created_by')
                LOGGER.info(f' 10) comparison is {answer}')

                try:
                    assert answer
                except AssertionError as e:
                    counter = next_sub_test(e, counter)
                    continue

        counter, success = end_loop(counter, success)
    LOGGER.info(f' Succeeded: {success} of {length}')


def test_get_object(client):
    counter: int = 1
    success: int = 0
    length: int = 0
    data: dict = {}

    data, length = start_test(data, length, 'get_object.json', 'test_get_object')

    for obj in data['tasks']:
        LOGGER.info(f' ##### TITLE : {obj["title"]} #####')
        LOGGER.info(f' Starting Test {counter}')
        LOGGER.info(f' 1) Posting {obj["object"]} to {obj["path"]}')
        path = obj['path']
        try:
            response = client.post(
                f'{path}?email=user@gmail.com',
                json=obj['object']
            )
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 2) Got response {response}')
        LOGGER.info(f' 3) Got response {response.json}')

        answer = response.status_code == HTTPStatus.CREATED
        LOGGER.info(f' 4) comparison is {answer} -> {response.status_code} =? {HTTPStatus.CREATED}')
        try:
            assert answer
        except AssertionError as e:
            counter = next_sub_test(e, counter)
            continue

        temp_id: str = response.json['_id']
        LOGGER.info(f' 6) Got id {temp_id}')
        LOGGER.info(f' 7) Checking if test {counter} is valid')
        if not obj['valid']:
            LOGGER.info(f' 8) Test {counter} is invalid')
            LOGGER.info(f' 9) temp_id is {temp_id} = {obj["id"]} obj["id"]')
            temp_id = obj['id']

        LOGGER.info(f' 10) Getting {obj["path"]}/{temp_id}')
        path = f'{obj["path"]}/{temp_id}'
        try:
            response = client.get(
                f'{path}?email=user@gmail.com',
            )
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 11) Got response {response}')
        LOGGER.info(f' 12) Got response {response.json}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f' 13) comparison is {answer}')
        try:
            assert answer
        except AssertionError as e:
            LOGGER.error(f' Failing in assert response Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 14) Checking if test {counter} is valid')
        if not obj['valid']:
            LOGGER.info(f' 15) Test {counter} is invalid')
            LOGGER.info(f' 16) succeeded {counter}')
            success += 1
            counter += 1
            continue

        LOGGER.info(f' 17) Comparing {response.json} to {obj["object"]}')
        answer = equal_dicts_only(response.json, obj['object'], 'type')
        LOGGER.info(f' 18) comparison is {answer}')

        try:
            assert answer
        except AssertionError as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 19) Checking if test {counter} has data')
        if 'data' in obj['object']:
            LOGGER.info(f' 20) Test {counter} has data')
            LOGGER.info(f' 21) Comparing {response.json} to {obj["object"]}')
            answer = equal_dicts_only(response.json, obj['object'], 'type', 'data')
            LOGGER.info(f' 22) comparison is {answer}')
            try:
                assert answer
            except AssertionError as e:
                counter = next_sub_test(e, counter)
                continue

        counter, success = end_loop(counter, success)
    LOGGER.info(f' Succeeded: {success} of {length} ')


def test_update_object(client):
    counter: int = 1
    success: int = 0
    length: int = 0
    data: dict = {}

    data, length = start_test(data, length, 'update_object.json', 'test_update_object')

    for obj in data['tasks']:
        LOGGER.info(f' ##### TITLE : {obj["title"]} #####')
        LOGGER.info(f'Starting {counter}')
        LOGGER.info(f' 1) Posting {obj["old_object"]} to {obj["path"]}')
        # Post object
        path = obj['path']
        try:
            response = client.post(
                f'{path}?email=user@gmail.com',
                json=obj['old_object']
            )
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 2) Got response {response}')
        LOGGER.info(f' 3) Got response {response.json}')
        try:
            assert response.status_code == HTTPStatus.CREATED
            LOGGER.info(f' response status code is {response.status_code} =? {HTTPStatus.CREATED}')
        except AssertionError as e:
            counter = next_sub_test(e, counter)
            continue

        # Put object
        LOGGER.info(f' 4) Putting {obj["changes"]} to {obj["path"]}/{response.json["_id"]}')
        path = f'{obj["path"]}/{response.json["_id"]}'

        try:
            response = client.put(
                f'{path}?email=user@gmail.com',
                json=obj['changes']
            )
        except Exception as e:
            counter = next_sub_test(e, counter)
            continue

        LOGGER.info(f' 5) Got response {response}')
        LOGGER.info(f' 6) Got response {response.json}')
        LOGGER.info(f' 7) Comparing response status code {response.status_code} to {HTTPStatus.NO_CONTENT}')
        if response.status_code != HTTPStatus.NO_CONTENT:
            LOGGER.info(f' 8) Test {counter} is invalid')
            continue

        LOGGER.info(f' 9) Checking if test status code is {obj["status_code"]}')
        answer = response.status_code == obj['status_code']
        LOGGER.info(f' 10) comparison is {answer}')
        try:
            assert answer
        except AssertionError as e:
            LOGGER.error(f' Failing in assert response Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        # Get Updated object
        LOGGER.info(f' 11) Getting {path}')

        try:
            response = client.get(
                f'{path}?email=user@gmail.com',
            )
        except Exception as e:
            LOGGER.error(f' Failing in get object -> {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        LOGGER.info(f' 12) Got response {response}')
        LOGGER.info(f' 13) Got response {response.json}')

        try:
            assert response.status_code == HTTPStatus.OK
            LOGGER.info(f' 14) response status code is {response.status_code} =? {HTTPStatus.OK}')
        except AssertionError as e:
            LOGGER.error(f' Failing in assert response Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            counter += 1
            continue

        try:
            assert equal_dicts_exclude(response.json, obj['new_object'], '_id', 'created_by')
            LOGGER.info(f' 15) Comparing {response.json} to {obj["new_object"]}')
        except AssertionError as e:
            LOGGER.error(f' Failing in assert response Got exception {e}')
            LOGGER.error(f' Failing test {counter}')
            continue

        counter, success = end_loop(counter, success)
    LOGGER.info(f' Succeeded: {success} of {length} ')
        
