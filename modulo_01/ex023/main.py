n=str(input('digite um numero: ')).rjust(4,'0')

print(f'unidade: {n[-1]}')
print(f'dezena: {n[-2]}')
print(f'centena: {n[-3]}')
print(f'milhar: {n[-4]}')