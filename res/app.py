import sys,random,string,pyperclip
from res.arth.console import *

sys.stdout.write("\x1b]2;passGen\x07")

def appTitle():
    clearConsole()
    print(consoleCharLightRed + '''
    █▀▀█ █▀▀█ █▀▀ █▀▀ ▒█▀▀█ █▀▀ █▀▀▄
    █░░█ █▄▄█ ▀▀█ ▀▀█ ▒█░▄▄ █▀▀ █░░█
    █▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▒█▄▄█ ▀▀▀ ▀░░▀
    ''')
    print(consoleCharLightBlack)

def askRequirements():
    while True:
        appTitle()
        passwordChars = input(
        f'''
        Select one option
        or just press Enter to select first option

        {consoleCharYellow}[1]{consoleCharLightBlack} All characters: Letters, numbers and symbols
        {consoleCharYellow}[2]{consoleCharLightBlack} All letters and numbers: {consoleCharWhite}No Symbols!{consoleCharLightBlack}
        {consoleCharYellow}[3]{consoleCharLightBlack} All letters and symbols: {consoleCharWhite}No Numbers!{consoleCharLightBlack}
        {consoleCharYellow}[4]{consoleCharLightBlack} Just letters: {consoleCharWhite}No numbers and symbols either{consoleCharLightBlack}

        ''')
        if passwordChars == '1' or passwordChars == '':
            caracteres = string.ascii_letters + string.digits + string.punctuation
            break
        elif passwordChars == '2':
            caracteres = string.ascii_letters + string.digits
            break
        elif passwordChars == '3':
            caracteres = string.ascii_letters + string.punctuation
            break
        elif passwordChars == '4':
            caracteres = string.ascii_letters
            break
        else:
            tryAgain()
    
    print()
    longitud = int(input('Password length: '))

    global password
    password = ''.join(random.choice(caracteres) for i in range(longitud))

def tryAgain():
    print(consoleCharRed)
    input('Please try again...' + consoleCharLightBlack)

def printPassAndClip():
    pyperclip.copy(password)
    print(consoleCharGreen)
    input('The password ' + consoleCharLightBlack + password + consoleCharGreen + ' has been copied!')
    print(consoleCharColorReset)
    clearConsole()

def printPass():
    print(consoleCharGreen)
    input('The password is ' + consoleCharLightBlack + password + consoleCharGreen)
    print(consoleCharColorReset)
    clearConsole()
