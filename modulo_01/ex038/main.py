nmr1=str(input('digite um valor: '))
nmr2=str(input('digite outro numero: '))

lst1=nmr1<nmr2
lst2=nmr2<nmr1


if lst1:
    print( f'o valor {nmr1} é maior!')

elif lst2:
    print(f'valor {nmr2} é maior!')

else:
    print('os numeros tem o msm valor!')  
