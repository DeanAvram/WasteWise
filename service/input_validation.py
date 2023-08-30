from flask import abort


class InputValidation:
    def __init__(self, *inputs: tuple, body: dict):
        self.inputs = inputs
        self.body = body
        self.validate(body)

    def validate(self, body: dict):
        for inp in self.inputs:
            if body[inp] is None:
                msg = inp + " is missing"
                abort(400, msg)
        return True
