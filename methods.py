import os
from create import createAccount, createProduct
import auth
import get


def signup():
    createAccount()


def login():
    auth.login(*get.getInputData('username', 'password'))


def logout():
    auth.logout()


def buy():
    user = get.getCurrentAccount()
    if user:
        _id = input('Enter ID of item to buy: ')
        product = get.getProducts(_id)
        if product['stock']>0:
            get.buyItem(_id)
        else:
            print('Not left in stocks')
    else:
        print('You should be logged in to add product.')


def add():
    user = get.getCurrentAccount()
    if user:
        if user['role']=='superUser':
            createProduct()
        else:
            print('You have not permission to add product.')
    else:
        print('You should be logged in to add product.')


def showAccount():
    user = get.getCurrentAccount()
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
    user = get.getCurrentAccount()
    categories = set([])
    if user:
        data = get.getProducts()
        for product in data:
            categories.add(product['category'])
        for category in categories:
            print(category)
    else:
        print('You should be logged in to show categories.')   


def showProducts():
    user = get.getCurrentAccount()
    if user:
        data = get.getProducts()
        for product in data:
            print(f"{product['id']} - {product['name']} - {product['price']} - {product['stock']} left")
    else:
        print('You should be logged in to show products.')

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
