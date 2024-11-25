total = cont = 0

n2 = int(input("digite um numero: "))
while n2 != 999:
    cont += 1
    total += n2
    n2 = int(input("digite um numero: "))

print(f"vc digitou {cont} numeros e a soma deles é: {total}")

print("fim")
