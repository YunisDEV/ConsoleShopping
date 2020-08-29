#!/usr/bin/env python3
from methods import *

if __name__ == '__main__':
    while True:
        try:
            cmd = input('>> ')
            if cmd == 'signup':
                signup()  # OK
            elif cmd == 'login':
                login()  # OK
            elif cmd == 'logout':
                logout()  # OK
            elif cmd == 'buy':
                buy()
            elif cmd == 'add':
                add()  # OK
            elif cmd[0:4] == 'show':
                subCmd = cmd.split(' ')[1]
                if subCmd == 'account':
                    showAccount()  # OK
                elif subCmd == 'categories':
                    showCategories()
                elif subCmd == 'products':
                    showProducts()
            elif cmd == 'help':
                help()  # FILL
            elif cmd == 'clear':
                clear()  # OK
            elif cmd == 'exit':
                clear()
                print('Thanks for using our services.')  # OK
                break
        except KeyboardInterrupt as e:
            clear()
            print('Thanks for using our services.')  # OK
            break
