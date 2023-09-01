from flask import abort
from http import HTTPStatus
import re


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
            elif 'mail' in inp:
                # The key contains the word 'mail' -> The value is mail
                self.validate_mail(body[inp])
        return True

    def validate_mail(self, mail: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, mail):
            abort(HTTPStatus.BAD_REQUEST, "Invalid mail")
        return True
