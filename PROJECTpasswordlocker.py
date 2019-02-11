#! python3
# PROJECTpasswordlocker - an insecure locker program

PASSWORDS = {'Khoa':'undertaker2279','Tho':'anhganhteam2K18','Thu':'Cheatonyou'}

import sys, pyperclip
# if len(sys.argv) < 2:
#     print('Usage: python pw.py [account] - copy account password')
#     sys.exit()
# account = sys.argv[1]

account = input('Please type in your username to retrieve the passowrd: ')

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passowrd for ' + account + ' copied to clipboard')

else:
    print('There is no account name ' + account)


