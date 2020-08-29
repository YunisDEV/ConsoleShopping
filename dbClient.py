import json
import os


class DBClient:
    def __init__(self, _file):
        self.file = _file

    def getDB(self):
        with open("db.json", 'rt') as read_file:
            return json.load(read_file)

    def addUser(self, obj):
        with open(self.file, 'w') as source:
            current = self.getDB()
            print(current)
            current.users.append(obj)
            json.dump(current, source)
            print('Successfully added user.')

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
