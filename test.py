import random

mylist = ["apple", "banana", "cherry"]
x = [2,3,21,312,31,31,3123,131]

print(mylist)
print(x)

random.shuffle(mylist)
random.shuffle(x)

print(x)
print(mylist)