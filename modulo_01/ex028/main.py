from random import choice

n = float(input("tente sua sorte na blaze: "))

n1 = [1, 2, 3, 4, 5]


n2 = choice(n1)

if n == n2:
    print(f"parabens vc acertou   ")

else:
    print("foi por pouco, mias sorte na proxima")
print(f"o pc escolheu: {n2}")
print("--fim--")
