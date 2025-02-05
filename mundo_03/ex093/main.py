lista = {}
golt = list()

lista["nome"] = input("Nome do jogador: ")
tot = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
for c in range(0, tot):
    golt.append(
        int(input(f'      Quantos gol {lista["nome"]} marcou na partida {c}? '))
    )
lista["gols"] = golt[:]
lista["total"] = sum(golt)

print("=-" * 15)
print(f"{lista}")
print("=-" * 15)

print(f'O campo nome tem o valor {lista["nome"]}')
print(f'O campo gols tem o valor {lista["gols"]}')
print(f"O campo total tem o valor {lista['total']}")
print("=-" * 15)
print(f'O jogsdor {lista["nome"]} jogou {tot} partidas ')
for i, v in enumerate(golt):
    print(f"      =>Na partida {i}, fez {v} gols")
print(f"O total foi de {lista['total']}")
