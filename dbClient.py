import json
import os


class DBClient:
    def __init__(self, _file):
        self.file = _file

    def getDB(self):
        with open("db.json", 'rt') as read_file:
            data = json.load(read_file)
            read_file.close()
            return data

    def addUser(self, obj):
        with open(self.file, 'w') as source:
            current = self.getDB()
            print(current)

    def getUser(self, _id):
        pass

    def deleteUser(self, _id):
        pass

    def addProduct(self, *args):
        pass

    def getProduct(self, _id=None):
        if _id == None:
            pass
        else:
            pass

    def deleteProduct(self, _id):
        pass


db = DBClient('db.json')