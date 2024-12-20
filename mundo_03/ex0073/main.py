tabela = (
    "Palmeiras",
    "Botafogo",
    "Internacional",
    "Fortaleza",
    "Flamengo",
    "Sao Paulo",
    "Cruzeiro",
    "Bahia",
    "Corinthians",
    "Atletico-MG",
    "Vasco da Gama",
    "EC Vitória",
    "Athletico-PR",
    "Grêmio",
    "Juventude",
    "Fluminense",
    "Criciuma",
    "Bragantino",
    "Cuiabá",
    "Atlético-Go",
)

print(tabela[0:5])
print("-" * 20)
print("ZONA DE REBAIXA MENTO")
print(tabela[16:20])
print("-" * 20)
print("TABELA EM ORDEM ALFABETICA")
print()
print(sorted(tabela))
confirmar = input("deseja saber a posicao de algum time S/N: ").upper()
if confirmar in "S":
    time = input("qual time do brasileirao serie A voce deseija saber ").upper()

    for i, v in enumerate(tabela):
        if v.upper() == time:
            print(str(i + 1) + "º")
