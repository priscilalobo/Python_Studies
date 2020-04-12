# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.

"""from random import choice
print('Vamos brincar de um jogo de adivinhação!\nEstá preparado?\nEntão vamos lá!')
n = input('Escolha um número de 0 a 5, se você adivinhar o meu número escolhido, ganha um prêmio: ')
lista = [0,1,2,3,4,5]
escolha = choice(lista)
if escolha == n:
    print('Você adivinhou =o, peça seu prêmio na recepção!')
else:
    print(f'Infelizmente você não acertou =(\n meu número escolhido foi {escolha} e não {n}')"""

#Outra forma de fazer

from random import randint
from time import sleep
computador = randint(0, 5)
print('Vamos brincar de um jogo de adivinhação!\nEstá preparado?\nEntão vamos lá!')
n = input('Escolha um número de 0 a 5, se você adivinhar o meu número escolhido, ganha um prêmio: ')
print('PROCESSANDO...')
sleep(2)
if n == computador:
    print('Você acertou!')
else:
    print(f'Você errou, meu número escolhido foi {computador} e não {n}')