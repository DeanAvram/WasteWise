from src.data.enum_object import EnumObject
from src.data.enum_role import EnumRole
from src.data.enum_commands import EnumCommands
from src.data.enum_periods import EnumPeriod

email_regex = "[A-Za-z]*[A-Za-z0-9]@([\w-]+\.)+[\w-]{2,4}$"
password_regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"

object_schema = {
    "title": "Object",
    "description": "A object request json",
    "type": "object",
    "properties": {
        "type": {
            "description": "The object of the user",
            "type": "string",
            "minLength": 1,
            "enum": [str(t.name) for t in EnumObject]
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
            "enum": [str(t.name) for t in EnumRole]
        },
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
            "enum": [str(t.name) for t in EnumRole]
        },
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
                "enum": [str(t.name) for t in EnumCommands]
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
                        "lng": {
                            "type": "number"
                        },
                        "lat": {
                            "type": "number"
                        }
                    },
                    "required": ["lng", "lat"],
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
                        "enum": [str(t.name) for t in EnumPeriod]
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

add_place_command_schema = {
    "title": "Create Place",
    "type": "object",
    "properties": {
        "type": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "location": {
                    "type": "object",
                    "properties": {
                        "lng": {
                            "type": "number"
                        },
                        "lat": {
                            "type": "number"
                        }
                    },
                    "required": ["lng", "lat"],
                    "additionalProperties": False
                }
            },
            "required": ["name", "location"],
            "additionalProperties": False
        }
    },
    "required": ["type", "data"],
    "additionalProperties": False
}


get_places_command_schema = {
    "title": "Places Command",
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
                        "lng": {
                            "type": "number"
                        },
                        "lat": {
                            "type": "number"
                        },
                    },
                    "required": ["lng", "lat"],
                    "additionalProperties": False
                },
                "radius": {
                    "type": "number"
                }
            },
            "required": ["location", "radius"],
            "additionalProperties": False
        }
    },
    "required": ["type", "data"],
    "additionalProperties": False
}

