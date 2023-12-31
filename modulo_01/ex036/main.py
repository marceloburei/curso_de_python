vlr1=int(input('qual valor da casa: '))
vlr2=int(input('qual valor do seu salario  : '))
vlr3=int(input('quantos anos deseja parcelar: '))

vlm=vlr1/(vlr3*12)
maxvalue=vlr2*0.7


if vlm <=  maxvalue :
    print('pode comprar')

else:
    print('nao foi possivel efetuar a compra')
