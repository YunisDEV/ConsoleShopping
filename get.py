import auth
from dbClient import db


def getInputData(*args):
    result = []
    for arg in args:
        result.append(input(str(arg).capitalize()+': '))
    return result


def getCurrentAccount():
    if auth.getCurrentID() == None:
        return None
    return db.getUser('_id', auth.getCurrentID())


def getProducts(_id=None):
    return db.getProduct(_id)


def buyItem(_id):
    db.buyItem(_id)
