mulher = homem = maior = 0


while True:
    idade = int(input("digite sua idade:").upper())
    sexo = input("digite seu sexo, M/F").upper()
    continuar = input("deseja continuar S/N").upper()
    if idade > 18:
        maior += 1

    if sexo in "M":
        homem += 1
    if sexo in "F":
        mulher += 1
    if continuar in "N":
        break

print(f"tem {maior} pessoas maior de 18 anos  ")
print(f"tem {homem} homens cadastrados  ")
print(f"tem {mulher} mulheres menor de 20 anos  ")
