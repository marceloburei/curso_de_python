total = inp = 0
numeros = []

# leia varios numeros
while inp != "pare":
    inp = input("digite um numero inteiro: ")

    if inp != "pare":
        valor = int(inp)
        numeros.append(valor)
        total = total + valor

# mostrar media entre todos
print(
    f"""vc digitou {len(numeros)} numeros:
      A media é: {total / len(numeros)}
      O maior é: {max(numeros)}
      O menor é: {min(numeros)}"""
)
