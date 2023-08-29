n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

def verifica():
    menor()
    maior()

def menor():
    if n1 < n2 and n1 < n3:
        return print(f"O menor número digitado é {n1}")
    elif n2 < n1 and n2 < n3:
        return print(f"O menor número digitado é {n2}")
    else:
        return print(f"O menor número digitado é {n3}")
    
def maior():
    if n1 > n2 and n1 > n3:
        return print(f"O maior número digitado é {n1}")
    elif n2 > n1 and n2 > n3:
        return print(f"O maior número digitado é {n2}")
    else:
        return print(f"O maior número digitado é {n3}")
    
verifica()