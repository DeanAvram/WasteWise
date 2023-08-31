from flask import abort
from http import HTTPStatus


class InputValidation:
    def __init__(self, *inputs: tuple, body: dict):
        self.inputs = inputs
        self.body = body
        self.validate(body)

    def validate(self, body: dict):
        for inp in self.inputs:
            if body[inp] is None:
                msg = inp + " is missing"
                abort(HTTPStatus.BAD_REQUEST, msg)
        return True
