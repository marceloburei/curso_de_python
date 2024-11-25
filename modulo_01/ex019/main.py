from random import choice

n1 = str(input("nome da pessoa: "))
n2 = str(input("nome da pessoa: "))
n3 = str(input("nome da pessoa: "))
n4 = str(input("nome da pessoa: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f"o escolhido foi {escolhido}")
