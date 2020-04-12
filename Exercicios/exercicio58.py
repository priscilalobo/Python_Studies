#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

"""from random import randint
computador = randint(0,10)
print(computador)
acertou = False
palpite = 0
print('Vamos brincar de jogo de adivinhação!')
print('Você terá que adivinhar qual o número de 0 a 10 o computador está pensando')
while not acertou:
    jogador = int(input('Digite um número de 0 a 10:  '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Tente um número menor')
        else:
            print('Tente um número maior')
print(f'Você adivinhou o número escolhido \o/ com {palpite} palpites') """





from random import randint
computador = randint(0,10)
#print(computador)
palpite = 0
acertou = False
print('Sou o seu computador')
print('Acabei de pensar em um número de 0 a 10')
while not acertou:
   jogador = (int(input('Tente adivinhar, chute um número de 0 a 10: ')))
   palpite +=1
   if jogador == computador:
      acertou = True
   else:
      if jogador > computador:
       print('Tente um número menor')
      else:
          print('Tente um número maior')
print(f'Você acertou o número que o computador escolheu foi {computador} e você acertou em {palpite} tentativas')













