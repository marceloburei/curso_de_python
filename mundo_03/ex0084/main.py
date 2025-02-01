listatds = []
cont = 0
maiorps = menorps = 0
princi = []

while True:
    listatds.append(input("digite seu nome: "))
    cont += 1
    listatds.append(float(input("digite seu peso: ")))

    if len(princi) == 0:
        maiorps = menorps = listatds[1]

    else:
        if listatds[1] > maiorps:
            maiorps = listatds[1]
    if listatds[1] < menorps:
        menorps = listatds[1]

    princi.append(listatds[:])
    listatds.clear()
    parar = input("deseja parar digite [N]: ").upper()
    if parar == "N":
        break
print(f"Foi cadastrado {cont} pessoas!")
print(f"o maior peso e : {maiorps}kg, esse peso e de =", end="")
for p in princi:
    if p[1] == maiorps:
        print(f"{p[0]}")
print(f"o menor peso e : {menorps}kg, esse peso e de =", end="")
for p in princi:
    if p[1] == menorps:
        print(p[0])
