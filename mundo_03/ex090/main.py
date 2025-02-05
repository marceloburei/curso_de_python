aluno = {}
aluno["nome"] = input("digite o nome: ")
aluno["media"] = float(input("qua e a media ? "))

print(f'O nome e igual : {aluno["nome"]} ')
print(f'A media e igual a: {aluno["media"]}')
if aluno["media"] < 6:
    print(" vc esta reprovado !!!")
else:
    print("vc passou !!! ")
