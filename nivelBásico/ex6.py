# Verifique se um número é primo.

num = int(input("Digite um número para verificar se é primo ou não: "))
i = 0
c = 0

while i <= num or c < 2:
    i = i + 1
    x = num % i 
    if x == 0:
        c = c + 1
if c <= 2:
    print(f"Número {num} é PRIMO!")
else:
    print(f"Número {num} NÃO É PRIMO!")