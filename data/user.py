import uuid
from role import Role


class User:
    def __init__(self, name: str, mail: str, password: str, role: Role):
        self.name = name
        self.mail = mail
        self.password = password
        self.id = uuid.uuid1()

    def get_name(self):
        return self.name

    def get_mail(self):
        return self.mail

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_id(self):
        return self.id


