n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
s = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('Sum = {}, the product is {}, and the division is {:.2f}'.format(s, m, d), end=' ')
print('Intereger division {} and pontecy {}'.format(di, e))