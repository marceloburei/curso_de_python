valor = float(input(" digite o valor da compra: "))

print("====temos essas formas de pagamento====")

print("1- avista: ")
print("2- avista no catao: ")
print("3- 2x no cartao de credito: ")
print("4- 3x ou mais:")
lista = int(input("qual deseja escolher? "))


if lista == 1:
    print(f"ficara {valor-valor*0.10} ")

elif lista == 2:
    print(f"ficara {valor-valor*0.5} ")

elif lista == 3:
    print(f"ficara {valor} ")

elif lista == 4:
    print(f"ficara {valor+valor*0.20} ")
else:
    print("desculpa nao entedi pode repetir?")
