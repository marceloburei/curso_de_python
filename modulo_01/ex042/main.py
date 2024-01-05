r1=int(input('digite o valor de uma reta '))
r2=int(input('digite o valor de uma reta '))
r3=int(input('digite o valor de uma reta '))

vld= r1+r2 <=r3 and r1 + r3 <= r2 and r2 + r3 <=r1
vld2= r1==r2 and r1==r3


if vld :
    print('um triangulo')

elif vld2 :
    print('isoceles')

else:
    print('escaleno')