lista = {}


lista["nome"] = input("nome: ")
lista["idade"] = int(input("Ano de nascimento: "))
lista["carteira"] = int(input("carteira de trabalho    (0 nao tem): "))

if lista["carteira"] != 0:
    lista["contratado"] = int(input("Ano q foi contratado contratado: "))
    lista["salario"] = int(input("salario: R$"))

print(f"o nome e {lista['nome']}")
print(f'tem  {2025- lista["idade"]} anos')
print(f'carteira de trabalho e : {lista["carteira"]}')


if lista["carteira"] != 0:
    print(f'foi contratado em {lista["contratado"]}')
    print(f"o salario e de: R${lista['salario']}")
    print(f"ira se aposentar com { (lista['contratado']+ 35)-lista['idade']}")
