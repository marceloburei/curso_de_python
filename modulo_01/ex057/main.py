sexo = str(input("digite seu sexo:[F/M] ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("dados invalido, porfavor tente denovo: ")).strip().upper()[0]
print(f"seoxo {sexo} registrado!")
