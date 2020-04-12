#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
# o menor peso lidos.

maior = 0
menor = 0
for peso in range(1,6):
    kilo = float(input(f'Qual o peso da {peso}º pessoa? '))
    if peso == 1:
        maior = kilo
        menor = kilo
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}\nO menor peso é {menor}')

