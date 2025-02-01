from random import randint

lista = list()
jogos = list()

print("~-" * 10)
print("MEGA SENA")
print("~-" * 10)


qnt = int(input("deseja quantos numero: "))
tot = 1
while tot <= qnt:
    cont = cont2 = 0
    while True:

        num = randint(1, 60)

        if num not in lista:

            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])

    lista.clear()
    tot += 1
print("=-" * 5, "  sorteando  ", "=-" * 5)
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")

print("=-" * 5, "  BOA SORTE  ", "=-" * 5)
