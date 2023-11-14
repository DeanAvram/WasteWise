from dataclasses import dataclass
import uuid
from src.data.enum_role import EnumRole
import json
from passlib.hash import pbkdf2_sha256


@dataclass
class User:
    _id: str
    name: str
    email: str
    password: str
    role: EnumRole

    def __init__(self, name: str, email: str, password: str, role: EnumRole):
        self._id = str(uuid.uuid1())
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_id(self):
        return self._id

    def set_password(self, password: str):
        self.password = password

    def __str__(self):
        return f'{self.name} {self.email} {self.password} {self.role}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def update(self, usr: dict):
        if 'name' in usr and usr['name'] is not None:
            self.name = usr['name']
        if 'email' in usr and usr['email'] is not None:
            self.email = usr['email']
        if 'password' in usr and usr['password'] is not None:
            self.password = pbkdf2_sha256.encrypt(usr['password'])
        if 'role' in usr and usr['role'] is not None:
            self.role = usr['role']
