#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns 
# termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeirotermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantas mais razões você quer? '))
print(f'A progressão foi finalizada com {total} termos mostrados')
