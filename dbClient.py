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

    def writeDB(self, data, dataName):
        with open(self.file, 'w') as source:
            json.dump(data, source)
            if dataName:
                print(f'Successfully added {dataName}.')

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
            self.writeDB(current, 'user')
        else:
            print('Username should be unique.')

    def getUser(self, _username):
        data = self.getDB()
        for u in data['users']:
            if u['username'] == _username:
                return u

    def getUserById(self, _id):
        data = self.getDB()
        for u in data['users']:
            if u['_id'] == _id:
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
            self.writeDB(current, 'product')
        else:
            print('Product id should be unique.')

    def getProduct(self, _id):
        if _id == None:
            data = self.getDB()
            return data['products']
        else:
            data = self.getDB()['products']
            for i in data:
                if i['id'] == _id:
                    return i

    def buyItem(self, _id):
        data = self.getDB()
        for i in range(len(data['products'])):
            if data['products'][i]['id'] == _id:
                data['products'][i]['stock'] -= 1
                print(f'Bought {data["products"][i]["name"]} for {data["products"][i]["price"]}')
                break
        self.writeDB(data,None)

    def deleteProduct(self, _id):
        pass


db = DBClient('db.json')
