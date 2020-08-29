import auth
from dbClient import db

getInputData = lambda *args : [input(str(arg).capitalize()+': ') for arg in args]


def getCurrentAccount():
    if auth.getCurrentID() == None:
        return None
    return db.getUser('_id', auth.getCurrentID())


def getProducts(_id=None):
    return db.getProduct(_id)


def buyItem(_id):
    db.buyItem(_id)
