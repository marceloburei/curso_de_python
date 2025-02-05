num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f"digite o {i} valor: "))

    if valor % 2 == 0:
        num[0].append(valor)

    else:
        num[1].append(valor)
print("=-=-" * 10)
num[0].sort()
num[1].sort()
print(f"os numero pares digitados foram:  {num[0]}")
print(f"os numero impares digitados foram: {num[1]}")
