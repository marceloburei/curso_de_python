import math

angulo=float(input('digite um valor: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno do ângulo {angulo} é {seno:.2f}')
print(f'O cosseno do ângulo {angulo} é {cosseno:.2f}')
print(f'A tangente do ângulo {angulo} é {tangente:.2f}')