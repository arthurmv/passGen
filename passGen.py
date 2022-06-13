import sys
import random
import string
import pyperclip
from os import system, name
from colorama import Fore, Back, Style

sys.stdout.write("\x1b]2;passGen\x07")

def clear(): 
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def app_title():
    clear()
    print(Fore.LIGHTRED_EX + '''
    █▀▀█ █▀▀█ █▀▀ █▀▀ ▒█▀▀█ █▀▀ █▀▀▄
    █░░█ █▄▄█ ▀▀█ ▀▀█ ▒█░▄▄ █▀▀ █░░█
    █▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▒█▄▄█ ▀▀▀ ▀░░▀
    ''')
    print(Fore.LIGHTBLACK_EX)

app_title()

while 1:
    try:
        longitud = int(input('Password length: '))
        break
    except ValueError:
        print(Fore.RED)
        input('Password lenght only...' + Fore.LIGHTBLACK_EX)
        app_title()

caracteres = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(caracteres) for i in range(longitud))

pyperclip.copy(password)

print(Fore.GREEN)
input('The password ' + Fore.LIGHTBLACK_EX + password + Fore.GREEN + ' has been copied!')
print(Fore.RESET)
clear()
