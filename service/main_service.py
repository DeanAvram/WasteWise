from pymongo import MongoClient


class MainService:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.wastewize

    def get_db(self):
        return self.db
