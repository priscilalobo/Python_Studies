# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, Calcule o mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente?'))
print(f'O valor da hipotenusa é {hypot(co,ca)}')
