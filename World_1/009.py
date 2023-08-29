# Write a program that reads a value in meters and displays it 
# converted into centimeters and millimeters.

n = float(input('Enter a number and see the conversion into centimeters and millimeters a number: '))
print('Cm: {}'.format(n * 100))
print('Mm: {}'.format(n * 1000))