"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro
de tinta, pinta uma área de 2m².
"""

alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Qual é a largura da sua parede? '))
area = alt*larg
tinta = area/2
print(f'Sua parede tem a dimensão de {alt}x{larg}, e sua área é de {area}m²')
print(f'Então você irá precisar de {tinta} litros de tinta')
