valor_total = maior_q_mil = 0
menor_preco = None
produto_menor_preco = ""

while True:
    print("-" * 30)
    print(" MERCADO BUREIS ")
    print("-" * 30)
    nome = input("digite o nome de seu produto:")
    preco = float(input("digite o preço de seu produto:"))
    continuar = input("desja continuar: S/N").upper()

    valor_total += preco

    if preco > 1000:
        maior_q_mil += 1

    if menor_preco is None or preco < menor_preco:

        menor_preco = preco

        produto_menor_preco = nome

    if continuar in "N":

        break
print("-" * 50)
print("FIM DO PROGRAMA  ")
print("-" * 50)
print(f"produto mais barato e : {produto_menor_preco} ")

print(f"total gasto e de: {valor_total}")

print(f"{ maior_q_mil} produtos custam mais de 1000")
