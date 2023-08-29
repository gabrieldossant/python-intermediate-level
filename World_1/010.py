# Multiplication table

n = int(input('Enter a number to see the multiplication table: ')) # User input

for i in range (1, 11): # Repetition structure to calculate the multiplication table
    print('{} x {} = {}'.format(n, i , n*i)) # Print to show the results