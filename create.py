from dbClient import db


def getInputData(*args):
    result = []
    for arg in args:
        result.append(input(str(arg)+': '))
    return result


def createAccount():
    params = ['Name', 'Username', 'Password']
    data = getInputData(*params)
    user = {}
    for i in range(len(params)):
        user[params[i]] = data[i]
    db.addUser(user)
