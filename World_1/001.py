import os

# Currency converter 

def chooseFrom():
    print("\n" * os.get_terminal_size().lines)
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
    print("\n" * os.get_terminal_size().lines)
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
        errorNumber()

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
    print("\n" * os.get_terminal_size().lines)
    brlCalculate(x)

def brlCalculate(x):
    if x == 1:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (BRL)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.20
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (BRL): R$ {} | (USD): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 2:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (BRL)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.18
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (BRL): R$ {} | (EUR): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 3:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (BRL)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.16
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (BRL): R$ {} | (GBP): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    else:
        errorChoose()

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
    print("\n" * os.get_terminal_size().lines)
    usdCalculate(x)

def usdCalculate(x):
    if x == 1:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (USD)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 4.92
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (USD): R$ {} | (BRL): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 2:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (USD)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.92
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (USD): R$ {} | (EUR): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 3:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (USD)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.78
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (USD): R$ {} | (GBP): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    else:
        errorChoose()

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
    eurCalculate(x)

def eurCalculate(x):
    if x == 1:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (EUR)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 4.92
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (EUR): R$ {} | (BRL): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 2:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (EUR)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.92
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (EUR): R$ {} | (USD): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 3:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (EUR)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 0.78
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (EUR): R$ {} | (GBP): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    else:
        errorChoose()

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
    gbpCalculate(x)

def gbpCalculate(x):
    if x == 1:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (GBP)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 6.24
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (GBP): R$ {} | (BRL): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 2:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (GBP)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 1.26
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (GBP): R$ {} | (USD): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    elif x == 3:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (GBP)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv * 1.16
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (GBP): R$ {} | (EUR): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()
    else:
        errorChoose()

def detailsAbbreviations():
    print('|----------------------------------|')
    print('| -   Details of Abbreviations   - |')
    print('|                                  |')
    print('| BRL = Real / Brazil              |')
    print('| USD = Dolar / American           |')
    print('| EUR = Euro                       |')
    print('| GBP = Pound Sterling             |')
    print('|                                  |')
    print('| by: Gabriel dos Santos Silva     |')
    print('|----------------------------------|')
    goBackMenu()     

def errorCaracter():
    print("\n" * os.get_terminal_size().lines)
    print('|----------------------------------|')
    print('| -- ! Unrecognizable command ! -- |')
    print('|----------------------------------|')
    print('| --  TYPE ONLY [ Y ] OR [ N ]  -- |')
    print('|----------------------------------|')
    goBackMenu()

def errorChoose():
    print("\n" * os.get_terminal_size().lines)
    print('|----------------------------------|')
    print('| -- ! Unrecognizable  NUMBER ! -- |')
    print('|----------------------------------|')
    print('| --         TYPE ONLY          -- |')
    print('|      [ 1 ] / [ 2 ] / [ 3 ]       |')
    print('|----------------------------------|')
    brl()

def errorNumber():
    print("\n" * os.get_terminal_size().lines)
    print('|----------------------------------|')
    print('| -- ! Unrecognizable  NUMBER ! -- |')
    print('|----------------------------------|')
    print('| --         TYPE ONLY          -- |')
    print('|  [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 0 ]   |')
    print('|----------------------------------|')
    goBackMenu()

def goBackMenu():
    r = input('| Go back to Menu? [Y]/[N]: ')
    if r.upper()[0] == "Y":
        print("\n" * os.get_terminal_size().lines)
        chooseFrom()
    elif r.upper()[0] == "N":
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| ---    CURRENCY CONVERSOR    --- |')
        print('|----------------------------------|')
        print('|         T H A N K  Y O U         |')
        print('|----------------------------------|s')
        exit()    
    else:
        errorCaracter()

chooseFrom()