#!/usr/bin/env python3
from methods import *

if __name__ == '__main__':
    while True:
        cmd = input('>> ')
        if cmd == 'signup':
            signup() #OK
        elif cmd == 'login':
            login() #OK
        elif cmd == 'logout':
            logout() #OK
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
