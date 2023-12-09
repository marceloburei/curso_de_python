n=str(input('digite o nome: ')).strip()

print(f'maiuscula : {n.upper ()}')
print(f'minuscula: {n.lower ()}')
print(f'o nome tem {len(n.replace(" ",""))} letras ')
print(f'o primeiro nome tem {n.find(" ")} letras')