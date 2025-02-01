f = str(input("digite uma frase: ")).upper().strip()

print(f'a frase tem: {f.count("A")} letras [A]')
print(f'ela aparece na posicao: {f.find("A")+1}')
print(f'ela aparece na posicao: {f.rfind("A")+1}')
