import identify

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
    identify.identifyFrom(f) 

chooseFrom()