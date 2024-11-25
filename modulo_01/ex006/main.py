while True:

    n1 = int(input("digite um numero: "))

    print("-" * 20)
    print(f"dobro: {n1 * 2}")
    print("-" * 20)
    print(f"triplo: {n1 * 3}")
    print("-" * 20)
    print(f"raiz quadrada: {n1 **(1/2) }")
    print("-" * 20)

    continuar = input(" para continuar ou parar digite: S/N ").upper()

    if continuar in "S":
        print()
    else:

        break
