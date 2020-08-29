from dbClient import db
from get import getInputData


def createAccount():
    params = ['name', 'username', 'password']
    data = getInputData(*params)
    user = {}
    for i in range(len(params)):
        user[params[i]] = data[i]
    db.addUser(user)
