# Arithmetical operations

n1 = int(input('Type a number: ')) # User input
n2 = int(input('Type another number: ')) # User input
s = n1 + n2 # Calculate a sum
m = n1 * n2 # Calculate the multiplication
d = n1 / n2 # Calculate the division
di = n1 // n2 # Calculate the integer division
e = n1 ** n2 # Calculate the exponentiation
print('Sum = {}, the product is {}, and the division is {:.2f}'.format(s, m, d), end=' ') # Printout to show the results of sum, mult and div
print('Intereger division {} and pontecy {}'.format(di, e)) # Printout to show the results of integer division and the exponentiation