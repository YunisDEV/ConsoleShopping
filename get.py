from auth import getCurrentID
from dbClient import db


def getInputData(*args):
    result = []
    for arg in args:
        result.append(input(str(arg).capitalize()+': '))
    return result


def getCurrentAccount():
    if getCurrentID() == None:
        return None
    return db.getUserById(getCurrentID())