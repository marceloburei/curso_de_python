lista = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze_lula_ladrao",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:

    numero = int(input("digite um numero entre 0 a 20: "))

    if 0 <= numero <= 20:
        break
    print(" nao foi possivel tente de novo ")
print(f"voce digitou o numero: {lista[numero]}")
