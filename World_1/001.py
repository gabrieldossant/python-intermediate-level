import os

# Currency converter 

def chooseFrom():
    print('|----------------------------------|')
    print('| ---    CURRENCY CONVERSOR    --- |')
    print('|----------------------------------|')
    print('| - FROM:                          |')
    print('| [ 1 ] BRL:                       |')
    print('| [ 2 ] USD:                       |')
    print('| [ 3 ] EUR:                       |')
    print('| [ 4 ] GBP:                       |')
    print('| [ 0 ] Details of abbreviations:  |')
    print('|----------------------------------|')
    f = int(input('| COIN : '))
    identifyFrom(f) 

def identifyFrom(x):
    if (x == 0):
        return detailsAbbreviations()
    elif (x == 1):
        return brl()
    elif (x == 2):
        return usd()
    elif (x == 3):
        return eur()
    elif (x == 4):
        return gbp()
    else:
        print('Invalid option.')
        print('Try Again.')
        chooseFrom()

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
    
def usd():
    print('|----------------------------------|')
    print('| ---    CURRENCY CONVERSOR    --- |')
    print('|----------------------------------|')
    print('| - TO:                            |')
    print('| [ 1 ] BRL:                       |')
    print('| [ 2 ] EUR:                       |')
    print('| [ 3 ] GBP:                       |')
    print('|----------------------------------|')
    x = int(input('| COIN : '))

def eur():
    print('|----------------------------------|')
    print('| ---    CURRENCY CONVERSOR    --- |')
    print('|----------------------------------|')
    print('| - TO:                            |')
    print('| [ 1 ] BRL:                       |')
    print('| [ 2 ] USD:                       |')
    print('| [ 3 ] GBP:                       |')
    print('|----------------------------------|')
    x = int(input('| COIN : '))

def gbp():
    print('|----------------------------------|')
    print('| ---    CURRENCY CONVERSOR    --- |')
    print('|----------------------------------|')
    print('| - TO:                            |')
    print('| [ 1 ] BRL:                       |')
    print('| [ 2 ] USD:                       |')
    print('| [ 3 ] EUR:                       |')
    print('|----------------------------------|')
    x = int(input('| COIN : '))

def detailsAbbreviations():
    print('|----------------------------------|')
    print('| -   Details of Abbreviations   - |')
    print('|                                  |')
    print('| BRL = Real / Brazil              |')
    print('| USD = Dolar / American           |')
    print('| EUR = Euro                       |')
    print('| GBP = Pound Sterling             |')
    print('|----------------------------------|')
    r = input('| Menu (Y)/(N): ')
    if r.upper()[0] == "Y":
        chooseFrom()
    elif r.upper()[0] == "N":
        exit()
    else:
        error(r)        

def error(res):
    print('|----------------------------------|')
    print('| --   Unrecognizable command   -- |')
    print('|                                  |')
    res = input('| Type ONLY (Y) OR (N): ')
    
chooseFrom()
