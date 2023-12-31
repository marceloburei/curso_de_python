nmr=int(input('digite u m numero: '))

print('''
escolha em qual base deseja converter 
[ 1 ] binario 
[ 2 ] octal 
[ 3 ] hexadecimal ''')
escolha=int(input('sua escolha: '))

if escolha == 1 :
    print(f'em binario: {bin(nmr)}')
elif escolha == 2:
    print(f'octal: {oct(nmr)}')
elif escolha == 3 :
    print(f'hexadecimal: {hex(nmr)}')
else:
    print('opcao invalida')