import json
import os
import uuid


class DBClient:
    def __init__(self, _file):
        self.file = _file

    def getDB(self):
        with open("db.json", 'rt') as read_file:
            return json.load(read_file)

    def writeDB(self, data, dataName):
        with open(self.file, 'w') as source:
            json.dump(data, source)
            if dataName:
                print(f'Successfully added {dataName}.')

    def addUser(self, obj):
        current = self.getDB()
        if len([i for i in current['users'] if i['username'] == obj['username']]) == 0:
            if obj['username'] == 'admin':
                obj['role'] = 'superUser'
            else:
                obj['role'] = 'user'
            obj['_id'] = str(uuid.uuid1())
            current['users'].append(obj)
            self.writeDB(current, 'user')
        else:
            print('Username should be unique.')

    def getUser(self, param, value):
        return [u for u in self.getDB()['users'] if u[param] == value][0]

    def addProduct(self, obj):
        current = self.getDB()
        if len([i for i in current['products'] if i['id'] == obj['id']]) == 0:
            obj['stock'] = int(obj['stock'])
            obj['price'] = float(obj['price'])
            current['products'].append(obj)
            self.writeDB(current, 'product')
        else:
            print('Product id should be unique.')

    def getProduct(self, _id):
        if _id == None:
            return self.getDB()['products']
        return [i for i in self.getDB()['products'] if i['id'] == _id][0]

    def buyItem(self, _id):
        data = self.getDB()
        for i in range(len(data['products'])):
            this = data['products'][i]
            if this['id'] == _id:
                data['products'][i]['stock'] -= 1
                print(f'Bought {this["name"]} for {this["price"]}')
                break
        self.writeDB(data, None)


db = DBClient('db.json')
