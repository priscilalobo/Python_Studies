#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

'''print(' 10 termos de uma PA')
termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão:'))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
print('Acabou')'''

num = int(input('\nDigite o Primeiro número da PA: '))
razão = int(input('Digite a Razão da PA: '))
for c in range(1, 11):
    print(num, end=' ')
    num += razão
print('Acabou')

