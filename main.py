from res.arth.console import *
from res.app import *

while True:
    try:
        askRequirements()
        break
    except ValueError:
        tryAgain()

while True:
    try:
        printPassAndClip()
        break
    except pyperclip.PyperclipException:
        printPass()
        break
