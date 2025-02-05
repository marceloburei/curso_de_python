lista = []
lista_impar = []
lista_par = []


while True:
    numero = int(input("digite um valor: "))
    parar = input("deseja continuar S/N: ")
    lista.append(numero)
    if numero % 2 == 0:
        lista_impar.append(numero)
    else:
        lista_par.append(numero)

    if parar == "n":
        break
print(f"os valores digitados foam: {lista}")
print(f"os valores pares sao : {lista_par}")
print(f"os valores impares sao : {lista_impar}")
