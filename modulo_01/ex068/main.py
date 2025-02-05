import random

cont = 0
while True:
    print("IMPAR OU PAR ")
    escolha = input("I\P: ").strip()
    numero = int(input("digite um numero: ").strip())

    ran = random.randint(0, 10)

    soma = numero + ran
    print(f"\033[92m Voce escolheu {numero}")
    print(f" Computador escolheu {ran}")
    print(f" Total {soma}")

    if escolha not in "PpIi":
        print("\033[91m Escolha invalida")
    elif escolha in "Pp" and soma % 2 == 0:
        print("\033[92m voce ganhou ")
    elif escolha in "Ii" and soma % 2 != 0:
        print("\033[92m voce ganhou i")
        cont += 1
    else:
        print("\033[91m voce perdeu")
        print(f"voce ganhou {cont} em seguida ")
        break
