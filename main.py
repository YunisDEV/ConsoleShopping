
from methods import *

if __name__ == '__main__':
    while True:
        cmd = input('>> ')
        if cmd == 'signup':
            signup()
        elif cmd == 'login':
            login()
        elif cmd == 'buy':
            buy()
        elif cmd == 'add':
            add()
        elif cmd[0:4] == 'show':
            subCmd = cmd.split(' ')[1]
            if subCmd == 'account':
                showAccount()
            elif subCmd == 'categories':
                showCategories()
            elif subCmd == 'products':
                showProducts()
        elif cmd == 'help':
            help()
        elif cmd == 'clear':
            clear()
        elif cmd == 'exit':
            print('Thanks for using our services.')
            break
