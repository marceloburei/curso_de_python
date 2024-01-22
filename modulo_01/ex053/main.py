palavra = str(input("digite uma palavra: ")).replace(" ", "")

invertida = palavra[::-1]

if palavra == invertida:
    print(" sua palavra e palindromo")

else:
    print("nao e palindromo")
