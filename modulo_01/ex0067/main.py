while True:
    n = int(input("digite o numero q deseja ver a tabuada:"))

    if n < 0:
        print("nao e possivel multiplicar com esse numero!")
        break

    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
