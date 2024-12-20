lista = []
cont = 0

while True:
    numero = int(input("digite um numero: "))
    parar = input("deseja continuar S/N: ").upper()

    lista.append(numero)
    lista.sort(reverse=True)
    cont += 1

    if parar == "N":
        break


print(f"foi digitado = {cont} numero ")
print(lista)

if 5 in lista:
    print("sim, o numero 5 esta na lista")
else:
    print("nao, o numero 5 nao esta na lista")
