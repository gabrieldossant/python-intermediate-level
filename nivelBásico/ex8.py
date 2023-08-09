word = input("Digite uma palavra: ")
inversor = ""

for i in word:
    inversor = i + inversor

if inversor == word:
    print(f"A palavra {inversor} é um palíndromo!")
else:
    print(f"A palavra {word} NÃO é um palíndromo!")