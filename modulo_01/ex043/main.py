import math

peso=float(input('digite seu peso: '))
altura=float(input('digite sua altura: '))

fimc= peso / (math.pow(altura,2))

ps1=  25 < 18 or 18 > 25
ps2=  25 > 30 or 30 < 25
ps3=  30 > 40 or 40 < 30

if 18.5 <= fimc :
    print('abaixo do peso ')

elif ps1 <= fimc :
    print('peso ideal')

elif ps2 <= fimc :
    print('sobre peso') 

elif ps3 <= fimc :
    print('obesidade') 
else :
    print('obesidade morbida')