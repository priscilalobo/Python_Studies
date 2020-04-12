#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('Iremos brincar de Jokenpô com o computador...vamos COMEÇAR!')
print('''Escolha:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA ''')
jogador = input('Qual a sua escolha? ')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print(f' O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
