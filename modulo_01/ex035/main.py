r1=int(input('digite o valor de uma reta '))
r2=int(input('digite o valor de uma reta '))
r3=int(input('digite o valor de uma reta '))

vld= r1+r2 >=r3 and r1 + r3 >= r2 and r2 + r3 >=r1

if vld :
    print('as retas formam um triangulo')
else:
    print('as retas nao formam um triangulo')