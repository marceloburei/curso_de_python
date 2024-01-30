menu = 4
while menu == 4:
    vlr1 = int(input("digite seu valor: "))
    vlr2 = int(input("digite seu valor: "))
    print("==== menu ====")

    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numero")
    print("[5] sair do programa\n")

    menu = int(input("qual deseja escolher?  "))


if menu == 1:
    print(f"seu valor ficou = {vlr1+vlr2}")

elif menu == 2:
    print(f"seu valor ficou = {vlr1*vlr2}")

elif menu == 3:
    print(f"seu valor ficou = {max([vlr1, vlr2])}")
elif menu == 5:
    print("ate mais")
else:
    print("opcao invalida")
