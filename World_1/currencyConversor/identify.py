import menu
import brl
import usd
import eur
import gbp
import details

def identifyFrom(x):
    if (x == 0):
        return details()
    elif (x == 1):
        return brl.brl()
    elif (x == 2):
        return usd()
    elif (x == 3):
        return eur()
    elif (x == 4):
        return gbp()
    else:
        print('Invalid option.')
        print('Try Again.')
        menu.chooseFrom()