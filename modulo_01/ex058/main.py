from random import choice

vezes = 0

n = int(input("tente sua sorte na blaze: "))

n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


n2 = choice(n1)
while n != n2:
    vezes += 1
    n = int(input("errado digite novamente: "))
print(f"o pc escolheu {n2}")
print(f" vc tentou {vezes} vezes")
print("--fim--")
