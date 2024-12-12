#! /usr/bin/env/ python3
#This project aims to store all the passwords for the respective application which makes user easier to remember complex password
#pw.py insecure password locker program
import pyperclip
PASSWORDS = {'email': 'alan@gmail.com',
             'blog': 'Hey Guys Alan here and this is my blog',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard. ')
else:
    print('There is no account name ' + account)
    