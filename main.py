#!/usr/bin/env python3
from methods import *

if __name__ == '__main__':
    while True:
        try:
            cmd = input('>> ')
            if cmd == 'signup':
                signup()
            elif cmd == 'login':
                login()
            elif cmd == 'logout':
                logout()
            elif cmd == 'buy':
                buy()
            elif cmd == 'add':
                add()
            elif cmd[0:4] == 'show':
                subCmd = cmd.split(' ')[-1]
                if subCmd == 'account':
                    showAccount()
                elif subCmd == 'categories':
                    showCategories()
                elif subCmd == 'products':
                    showProducts()
            elif cmd == 'help':
                help()  # FILL
            elif cmd == 'clear':
                clear()
            elif cmd == 'exit':
                clear()
                print('Thanks for using our services.')
                break
        except KeyboardInterrupt as e:
            clear()
            print('Thanks for using our services.')
            break
