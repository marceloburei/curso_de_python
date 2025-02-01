ficha = list()
while True:
    name = input("Nome: ")
    nt1 = float(input(" Nota 1: "))
    nt2 = float(input("nota 2: "))
    pare = input("deseja para ? ").upper()
    media = (nt1 + nt2) / 2
    ficha.append([name, [nt1, nt2], media])
    if pare == "S":
        break
print("=-" * 25)
print(f"{'Nº.':<5}     {'nome':<10}     {'media':>15}")

for i, l in enumerate(ficha):
    print(f"{i:<3}       {l[0]:<10}     {l[2]:>15}  ")
print("=-" * 25)
while True:

    opc = int(input("deseja saber nota de qual aluno?      [999 enterrompe] "))

    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print("-" * 25)
        print(f"as notas de {ficha[opc][0]} sao: {ficha[opc][1]}")
        print("-" * 25)
