from os import system,name

def clearConsole():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

while True:
    try:
        from res.arth.miConsole.colors import *
        break
    except ImportError:
        from miConsole.colors import *
        clearConsole()
        print(consoleCharGreen + "It's working!")
        print(consoleCharColorReset)
        break
