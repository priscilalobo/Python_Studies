# Calcule o seno, coseno e tangente

from math import sin,cos,tan,radians
a = int(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {a} tem o SENO de {sin(radians(a)):.2f}º')
print(f'O ângulo de {a} tem o COSSENO de {cos(radians(a)):.2f}º')
print(f'O ângulo de {a} tem a TANGENTE de {tan(radians(a)):.2f}°')

