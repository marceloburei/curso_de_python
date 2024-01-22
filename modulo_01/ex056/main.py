todas_idade = 0
media = 0
maiorhomem = 0
nomemaisvelho = ""
totmulher = 0
for c in range(1, 5):
    nome = str(input("digite seu nome: ")).strip()
    idade = int(input("digite sua idade: "))
    sexo = str(input("digite seu sexo masculino ou feminino: ")).strip()

    if c == 1 and sexo in "Mm":
        nomemaisvelho = idade

    if sexo in "Mm" and idade > maiorhomem:
        maiorhomem = idade
        nomemaisvelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher += 1
todas_idade += idade
media = todas_idade / 4

print(f"a media de idade do grupo é: {media}")
print(f"o homem mais velho tem: {maiorhomem}e se chama {nomemaisvelho}")
print(f"ao todo sao {totmulher}com menos de 20 anos")
