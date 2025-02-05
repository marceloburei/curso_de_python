maior = coluna = par = 0
lista = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
for l in range(0, 3):
    for i in range(0, 3):
        lista[l][i] = int(input(f"digite o numero  da posicao {l}x{i}: "))
print("-=" * 20)
for l in range(0, 3):
    for i in range(0, 3):
        print(f"[{lista[l][i]:^5}]", end="")

        if lista[l][i] % 2 == 0:
            par += lista[l][i]

    print()

for l in range(0, 3):
    coluna += lista[l][2]
print("-=" * 20)

print(f" a soma dos numeros da terceira coluna e : {coluna}")
print(f" a soma dos numeros pares e : {par}")
for i in range(0, 3):
    if i == 0:
        maior = lista[1][i]
    elif lista[1][i] > maior:
        maior = lista[1][i]
print(f"O maior numero da segunda fileira  foi: {maior}")
