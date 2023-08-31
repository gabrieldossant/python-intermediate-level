import os
import goBackMenu

def brlC(x):
    if x == 1:
        print('|----------------------------------|')
        print('| ---   ENTER A NUMBER  (BRL)  --- |')
        print('|----------------------------------|')
        conv = float(input('| : '))
        res = conv / 4.90
        print("\n" * os.get_terminal_size().lines)
        print('|----------------------------------|')
        print('| (BRL): R$ {} | (USD): R$ {:.1f}  |'.format(conv, res))
        print('|----------------------------------|')
        print('|                                  |')
        goBackMenu()