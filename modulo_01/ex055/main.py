maior_peso = 0
menor_peso = 9999999999
for c in range(1, 6):
    peso = int(input(f"digite o seu peso {c}: "))

    if peso > maior_peso:
        maior_peso = peso
    if menor_peso > peso:
        menor_peso = peso

print(f"{menor_peso} menor")
print(f"{maior_peso} maior")
