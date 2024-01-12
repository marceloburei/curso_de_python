n = 0
for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            n += num
print(f"A soma dos múltiplos é: {n}")
