aberto = fechado = 0
numero = input("digite uma expressao: ")
if numero == "(":
    aberto += 1
elif numero == ")":
    fechado += 1

if aberto == fechado:
    print(" sua expressao e valida")
else:
    print(" sua expressao nao e valida")
