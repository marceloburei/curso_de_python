cont = s = n = 0

while True:
    n = int(input("digite um numero:"))
    if n == 999:
        break
    s += n
    cont += 1
print(f"A soma entre os numeros e: {s}!")
print(f"foi digitado {cont} numeros!")
