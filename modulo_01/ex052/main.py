num = int(input("\nDigite um numero inteiro para saber se é primo: "))
div = []

for i in range(num):
    if num % (i + 1) == 0:
        div.append(i + 1)


if len(div) == 2:
    print("O numero é primo divisivel por ", div)

else:
    print("O numero nao e primo divisivel por", div)
