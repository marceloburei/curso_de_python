from random import choice

print(f"{'='*10} vamos jogar jokenpo {'='*10}")
print("1- pedra ")
print("2- papel ")
print("3- tisoura ")
player = int(input("escolha um: "))

pc = choice([1, 2, 3])

print(f"O computador escolheu: {pc}, Você: {player}")

if player == pc:
    print("empate")

elif pc == 1:
    if player == 2:
        print("vc ganhou")
    else:
        print("vc perdeu")

elif pc == 2:
    if player == 3:
        print("vc ganhou")
    else:
        print("vc perdeu")

elif pc == 3:
    if player == 1:
        print("vc ganhou")
    else:
        print("vc perdeu")
