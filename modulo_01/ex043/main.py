import math

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

fimc = peso / (math.pow(altura, 2))
if fimc <= 18.5:
    print("abaixo do peso ")
elif fimc <= 25:
    print("peso ideal")

elif fimc <= 30:
    print("sobre peso")

elif fimc <= 40:
    print("obesidade")
else:
    print("obesidade morbida")
