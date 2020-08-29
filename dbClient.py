import json
import os
import uuid


class DBClient:
    def __init__(self, _file):
        self.file = _file

    def getDB(self):
        with open("db.json", 'rt') as read_file:
            data = json.load(read_file)
            read_file.close()
            return data

    def writeDB(self,data,dataName):
        with open(self.file, 'w') as source:
            json.dump(data, source)
            print('Successfully added {dataName}.')

    def addUser(self, obj):
        current = self.getDB()
        unique = True
        for i in current['users']:
            if i['username'] == obj['username']:
                unique = False
                break
        if unique:
            data = obj
            if obj['username'] == 'admin':
                data['role'] = 'superUser'
            else:
                data['role'] = 'user'
            data['_id'] = str(uuid.uuid1())
            current['users'].append(data)
            self.writeDB(current,'user')
        else:
            print('Username should be unique.')

    def getUser(self, _username):
        data = self.getDB()
        for u in data['users']:
            if u['username']==_username:
                return u
    def getUserById(self,_id):
        data = self.getDB()
        for u in data['users']:
            if u['_id']==_id:
                return u
    def deleteUser(self, _id):
        pass

    def addProduct(self, obj):
        current = self.getDB()
        unique = True
        for i in current['products']:
            if i['id'] == obj['id']:
                unique = False
                break
        if unique:
            data = obj
            data['stock'] = int(data['stock'])
            data['price'] = float(data['price'])
            current['products'].append(data)
            self.writeDB(current,'product')
        else:
            print('Product id should be unique.')

    def getProduct(self, _id=None):
        if _id == None:
            pass
        else:
            pass

    def deleteProduct(self, _id):
        pass


db = DBClient('db.json')
