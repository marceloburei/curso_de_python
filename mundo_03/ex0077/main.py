palavras = (
    "algodao",
    "sofa",
    "chinelo",
    "teclado",
    "sapato",
    "programar",
    "estante",
    "armario",
    "marcelo",
    "perfume",
)
for p in palavras:
    print(f"\n Na palavra {p.upper()} temos: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f" {letra}", end="")
