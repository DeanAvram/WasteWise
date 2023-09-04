from flask import abort
from http import HTTPStatus
import re


class InputValidation:
    def __init__(self, *inputs: tuple, request_name: str, body: dict):
        self.inputs = inputs
        self.request_name = request_name
        self.body = body
        self._validate(body)

    def _validate(self, body: dict):
        for inp in self.inputs:
            match self.request_name.upper():
                case "POST":
                    # Check that all necessary inputs are in the body
                    if body[inp] is None:
                        msg = inp + " is missing"
                        abort(HTTPStatus.BAD_REQUEST, msg)
                    if 'mail' in inp:
                        # The key contains the word 'mail' -> The value is mail
                        self._validate_mail(body[inp])
                case "PUT":
                    # Check that values that not need to be changed are not changed
                    if inp == 'type' and body[inp] is not None:
                        abort(HTTPStatus.BAD_REQUEST, "Can't Change Object's type")
                    if inp == 'created_by' and body[inp] is not None:
                        abort(HTTPStatus.BAD_REQUEST, "Can't Change Object's created_by")
                    if inp == 'role' and body[inp] is not None:
                        abort(HTTPStatus.BAD_REQUEST, "Can't Change User's role")
                    if 'mail' in inp and body[inp] is not None:
                        # The key contains the word 'mail' -> The value is mail
                        self._validate_mail(body[inp])

        return True

    def _validate_mail(self, mail: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, mail):
            abort(HTTPStatus.BAD_REQUEST, "Invalid mail")
        return True
