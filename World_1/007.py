# Create an algorithm that reads a number and shows its double, triple and square root

n = int(input('Enter a number: '))
print('Double: {}'.format(n*n))
print('Triple: {}'.format(n*n*n))
print('Square root: {:.2f}'.format(n**(1/2)))
