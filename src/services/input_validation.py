from src.data.role import Role
from src.services.commands.commands import Commands, Period

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
            "minLength": 1,
            "axis": {
                "enum": Role
            }
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
            "minLength": 1,
            "axis": {
                "enum": Role
            }
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
            "minLength": 1,
            "axis": {
                "enum": Commands
            }
        },
        "data": {
            "description": "The data of the command",
            "type": "object",
        }
    },
    "required": [
        "type",
        "data"
    ],
    "additionalProperties": False
}

direct_command_schema = {
    "title": "Direct Command",
    "type": "object",
    "properties": {
        "type": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "object",
                    "properties": {
                        "lat": {
                            "type": "number"
                        },
                        "lng": {
                            "type": "number"
                        }
                    },
                    "required": ["lat", "lng"],
                    "additionalProperties": False
                }
            },
            "required": ["location"],
            "additionalProperties": False
        }
    },
    "required": ["type", "data"],
    "additionalProperties": False
}

history_command_schema = {
    "title": "History Command",
    "type": "object",
    "properties": {
        "type": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "period": {
                    "type": "string",
                    "axis": {
                        "enum": Period
                    }
                }
            },
            "required": ["period"],
            "additionalProperties": False
        }
    },
    "required": ["type"],
    "additionalProperties": False
}
