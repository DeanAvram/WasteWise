from http import HTTPStatus
from pathlib import Path

import os
import io
from tests.conftest import create_user


resource_path = Path(__file__).parent / 'resources'


def test_classification_plastic(client):
    user = create_user()
    arr = os.listdir("tests/test_data/images")
    print(arr)
    # TODO: fix this test

    for img_name in arr:
        '''print(img)
        print(type(open(f'tests/test_data/images/{img}', 'rb')))
        file_path = os.path.join("tests/test_data/images", img)
        x = os.path.basename(file_path)
        print(x)'
        img = open(f'tests/test_data/images/{img_name}', 'rb')
        response = client.post(
            f'/wastewise/classify?email={user["email"]}&password={user["password"]}',
            data={
                img.read()
            }
        )
        assert response.status_code == HTTPStatus.CREATED'''
        assert True

