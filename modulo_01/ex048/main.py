n = 0
for num in range(3, 501, 3):
    if num % 2 != 0:
        if num % 3 == 0:
            n = n + num
print(f"A soma dos múltiplos é: {n}")
