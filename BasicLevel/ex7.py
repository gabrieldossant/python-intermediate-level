# Calcule o fatorial de um número.

num = int(input("Digite um número ver o fatorial: "))
fat = 0
i = 1

while i < num:
    fat = num * i
    i += i

print(fat)