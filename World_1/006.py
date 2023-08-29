# Create a program in which the user types in a number and it 
# shows the predecessor and successor of this number. 

num = int(input('Enter any number: ')) # User input
print('The successor of this number is {}'.format(num+1), end=' ') 
print('The predecessor of this number is {}'.format(num-1))