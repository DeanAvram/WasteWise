email_regex = "[A-Za-z]*[A-Za-z0-9]@([\w-]+\.)+[\w-]{2,4}$"
password_regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"

object_schema = {
    "title": "Object",
    "description": "A object request json",
    "type": "object",
    "properties": {
        "type": {
            "description": "The type of the object",
            "type": "string",
            "minLength": 1
        },
        "created_by": {
            "description": "The user that created the object",
            "type": "string",
            "minLength": 1
        },
        "data": {
            "description": "The data of the object",
            "type": "object",
        },
        "active": {
            "description": "The active status of the object",
            "type": "boolean"
        }
    },
    "required": [
        "type",
        "created_by"
    ],
    "additionalProperties": False
}

object_schema_update = {
    "title": "Object",
    "description": "A object request json",
    "type": "object",
    "properties": {
        "active": {
            "description": "The active status of the object",
            "type": "boolean"
        },
        "data": {
            "description": "The data of the object",
            "type": "object",
        }
    },
    "additionalProperties": False
}

user_schema = {
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
            "pattern": email_regex
        },
        "password": {
            "description": "The password of the user",
            "type": "string",
            "minLength": 8,
            "maxLength": 16,
            "pattern": password_regex
        },
        "role": {
            "description": "The role of the user",
            "type": "string",
            "minLength": 1
        }
    },
    "required": [
        "name",
        "email",
        "password",
        "role"
    ],
    "additionalProperties": False
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
        "password": {
            "description": "The password of the user",
            "type": "string",
            "minLength": 8,
            "maxLength": 16,
            "pattern": password_regex
        },
        "role": {
            "description": "The role of the user",
            "type": "string",
            "minLength": 1
        }
    },
    "additionalProperties": False
}

command_schema = {
    "title": "Command",
    "description": "A command request json",
    "type": "object",
    "properties": {
        "type": {
            "description": "The type of the command",
            "type": "string",
            "minLength": 1
        },
        "invoked_by": {
            "description": "The user that invoked the command",
            "type": "string",
            "minLength": 1
        },
        "data": {
            "description": "The data of the command",
            "type": "object",
        },
        "created_at": {
            "description": "The time the command was created",
            "type": "number"
        }
    },
    "required": [
        "type",
        "invoked_by",
        "created_at"
    ],
    "additionalProperties": False
}
