maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input(f"digite o {c}º ano: "))
    if ano <= 2006:
        maiores = maiores + 1
    else:
        menores = menores + 1
print(f"{maiores} sao de maiores")
print(f"{menores} sao de menores")
