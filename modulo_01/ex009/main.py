cont = 0
n1 = int(input("digite a tabuada que voce deseja ver: "))

for i in range(0, 10):
    cont += 1
    print(f" {n1} x {cont} = {n1 * cont}")

print(4 * "~", "FIM", "~" * 4)
