from methods import getInputData
from dbClient import db

def createAccount():
    params = ['Name','Username','Password']
    data = getInputData(*params)
    user = {}
    for i in range(len(params)):
        user[params[i]] = data[i]
    db.addUser(user)