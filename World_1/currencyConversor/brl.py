import brlCalculate

def brl():
    print('|----------------------------------|')
    print('| ---    CURRENCY CONVERSOR    --- |')
    print('|----------------------------------|')
    print('| - TO:                            |')
    print('| [ 1 ] USD:                       |')
    print('| [ 2 ] EUR:                       |')
    print('| [ 3 ] GBP:                       |')
    print('|----------------------------------|')
    x = int(input('| COIN : '))
    brlCalculate.brlC(x)