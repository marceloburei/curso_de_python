numero9 = 0
numero_par = []
todos_valores = []

for i in range(0, 4):
    valor = int(input("digite um numero: "))
    todos_valores.append(valor)

    if valor == 9:
        numero9 += 1
    print("-" * 20)

    if valor % 2 == 0:
        numero_par.append(valor + 0)

    if valor == 3:
        primeiro = i + 1


print(f"VOCE DIGITOU: {todos_valores} ")
print("-" * 20)
print(f"O PRIMEIRO NUMERO 3 DIGITADO ESTA NA POSICAO: {todos_valores.index(3+1)} ")
print("-" * 20)

print(f"FOI DIGITADO  ({numero9}) NUMERO 9")
print("-" * 20)

print(f"NUMEREOS PARES DIGITADOS: {numero_par}")
print("-" * 20)
