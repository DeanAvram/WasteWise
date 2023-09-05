from flask import abort
from http import HTTPStatus
import re
from jsonschema import validate


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



object_schema = {
   "title":"Object",
   "description":"A object request json",
   "type":"object",
   "properties":{
        "type":{
            "description":"The type of the object",
            "type":"string",
            "minLength": 1
        },
        "created_by":{
            "description":"The user that created the object",
            "type":"string",
            "minLength": 1
        },
        "data":{
            "description":"The data of the object",
            "type":"object",
        }
   },
   "required":[
      "type",
      "created_by"
   ]
}

object_schema_update = {
    "title":"Object",
    "description":"A object request json",
    "type":"object",
    "properties":{
        "active":{
            "description":"The active status of the object",
            "type":"boolean"
        },
        "data":{
            "description":"The data of the object",
            "type":"object",
        }
    }
}

user_schema = {
    "title":"User",
    "description":"A user request json",
    "type":"object",
    "properties":{
        "name":{
            "description":"The name of the user",
            "type":"string",
            "minLength": 1
        },
        "email":{
            "description":"The email of the user",
            "type":"string",
            "format":"email"
        },
        "password":{
            "description":"The password of the user",
            "type":"string",
            "minLength": 8,
            "maxLength": 16,
            "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        },
        "role":{
            "description":"The role of the user",
            "type":"string",
            "minLength": 1
        }
    },
    "required":[
        "name",
        "email",
        "password",
        "role"
    ]
}

user_schema_update = {
    "title": "User",
    "description": "A user request json",
    "type": "object",
    "properties": {
        "name": {
            "description": "The name of the user",
            "type": "string",
            "minLength": 1
        },
        "email": {
            "description": "The email of the user",
            "type": "string",
            "format": "email"
        },
        "password": {
            "description": "The password of the user",
            "type": "string",
            "minLength": 8,
            "maxLength": 16,
            "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        },
        "role": {
            "description": "The role of the user",
            "type": "string",
            "minLength": 1
        }
    }
}

command_schema = {
    "title":"Command",
    "description":"A command request json",
    "type":"object",
    "properties":{
        "type":{
            "description":"The type of the command",
            "type":"string",
            "minLength": 1
        },
        "invoked_by":{
            "description":"The user that invoked the command",
            "type":"string",
            "minLength": 1
        },
        "data":{
            "description":"The data of the command",
            "type":"object",
        },
        "created_at":{
            "description":"The time the command was created",
            "type":"number"
        }
    },
    "required":[
        "type",
        "invoked_by",
        "created_at"
    ]
}