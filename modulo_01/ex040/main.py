md1=int(input('digite sua nota: '))
md2=int(input('digete outra nota: '))

media=(md1+ md2) /2

if media<=5.0 :
    print('reprovado!')

elif media<=6.9 : 
    print('recuperacao')

else:
    print('aprovado')