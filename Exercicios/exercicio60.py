#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite o número da fatorial: '))
c = n
f = 1
print(f'Calculando fatorial de {n}! ', end=' ')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end=' ')
    f*= c
    c -= 1
print(f'{f}')

