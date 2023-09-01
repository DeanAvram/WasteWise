import uuid
from src.data.role import Role
import json


class User:
    def __init__(self, name: str, email: str, password: str, role: Role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self._id = str(uuid.uuid1())

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

    def __str__(self):
        return f'{self.name} {self.email} {self.password} {self.role}'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
