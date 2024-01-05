from random import choice
print('==== vamos jogar jokenpo====')
print('1- pedra ')
print('2- papel ')
print('3- tisoura ')

lista=[1,2,3]
escolhido=choice(lista)
p=int(input('escolha um '))
print(f'{escolhido}')

if p < escolhido :
    print('computador ganhou')

elif p == escolhido :
    print('empate')

else :
    print(' vc ganhou')

