lista = []
for i in range(0, 5):
    numero = int(input("digite um valor: "))

    if not lista or numero <= lista[0]:
        lista.insert(0, numero)
        print("Adicionado na pozição 0")
    elif numero >= lista[-1]:
        lista.append(numero)
        print("Adicionado na ultima posicao")
    else:
        for i, n in enumerate(lista):
            if numero <= n:
                lista.insert(i, numero)
                print(f"Adicionado na posicao {i}")
                break


print(lista)
