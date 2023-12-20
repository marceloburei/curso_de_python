f=str(input('digite uma frase: ')).upper() .strip()

print(f'A frase tem: {f.count("A")}')
print(f'ela aparece na posicao: {f.find("A")+1}')
print(f'ela aparece na posicao: {f.rfind("A")+1}')
