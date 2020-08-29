import os
from create import createAccount, createProduct
import auth
from get import getInputData, getCurrentAccount


def signup():
    createAccount()


def login():
    auth.login(*getInputData('username', 'password'))


def logout():
    auth.logout()


def buy():
    print('BUY')


def add():
    user = getCurrentAccount()
    if user:
        if user['role']=='superUser':
            createProduct()
        else:
            print('You have not permission to add product.')
    else:
        print('You should be logged in to add product.')


def showAccount():
    user = getCurrentAccount()
    if user:
        if user['role']=='superUser':
            print('====ADMIN====')
        print(f"ID      : {user['_id']}")
        print(f"Name    : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Password: {'*'*len(user['password'])}")
    else:
        print('You have not logged in.')


def showCategories():
    print('SHOW CATEGORIES')


def showProducts():
    print('SHOW PRODUCTS')


def help():
    print('HELP')
    #FILL IT


def clear():
    clearString = ''
    if os.name == 'nt':
        clearString = 'cls'
    else:
        clearString = 'clear'
    os.system(clearString)
