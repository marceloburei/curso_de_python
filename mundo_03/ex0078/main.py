listanum = []
maior = 0
menor = 0
for i in range(0, 5):
    listanum.append(int(input(f"digite um valor para a posicao: {i} ")))

    if i == 0:
        maior = menor = listanum[i]
    else:
        if listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]
print("~" * 46)
print(f"voce digitou{listanum}")

print(f"O maior numero digitado e: {maior}, e esta nas posicoes: ", end="")
for c, v in enumerate(listanum):
    if v == maior:
        print(f"{c+1}...", end="")
print(f"\nO menor numero digitado e: {menor}, e esta nas posicoes: ", end="")
for c, v in enumerate(listanum):
    if v == menor:
        print(f"{c+1}...", end="")
