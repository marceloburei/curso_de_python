lista = (
    " teclado ",
    130.00,
    " Abafadores de som ",
    50.21,
    " Abafadores para chaleiras ",
    23.22,
    " processador ",
    760.00,
    " Abajur ",
    321.19,
    " Abóboras ",
    5.00,
    " Abobrinhas ",
    12.00,
    " monitor ",
    1200.00,
    " Abotoadeiras ",
    39.99,
    " carteira ",
    76.980,
    " Abraçadeiras de metal ",
    12.22,
    " enforca gato 10x ",
    44.99,
)
print(f"_" * 30)
print("LISTA DE PRODUTOS")
print(f"_" * 30)


for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end="")
    else:
        print(f"RS{lista[i]:>7.2f}")
