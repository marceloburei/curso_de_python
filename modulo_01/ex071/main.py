print("=" * 30)
print("caixa eletronico")
print("=" * 30)


saque = int(input("Digite o valor do saque: "))

total = saque
nota = 100
totalnotas = 0


while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f"Total de {totalnotas} notas de R$ {nota}")
        if nota == 100:
            nota = 50
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totalnotas = 0
        if total == 0:
            break
