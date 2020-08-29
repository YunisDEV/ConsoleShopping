import os
from create import createAccount


def signup():
    createAccount()


def login():
    print('LOGIN')


def buy():
    print('BUY')


def add():
    print('ADD')


def showAccount():
    print('SHOW ACCOUNT')


def showCategories():
    print('SHOW CATEGORIES')


def showProducts():
    print('SHOW PRODUCTS')


def help():
    print('HELP')


def clear():
    clearString = ''
    if os.name == 'nt':
        clearString = 'cls'
    else:
        clearString = 'clear'
    os.system(clearString)

