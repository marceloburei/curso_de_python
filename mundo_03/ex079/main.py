lista = []

while True:
    numero = int(input("digite um valor: "))
    print("valor adicionado...")
    if numero not in lista:
        lista.append(numero)
    continuar = input("deseja continuar: [S/N] ").upper()

    if continuar == "N":
        break
print("=-" * 25)
print(f"Os numeros digitados foram : {sorted(lista)}")
