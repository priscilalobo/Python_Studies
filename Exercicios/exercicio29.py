# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
velocidade = int(input('Informe a velocidade do carro: '))
print('Verificando a velocidade máxima utilizada nessa rodovia...')
sleep(2)
if velocidade >=80:
    print(f'A VELOCIDADE DESSA VIA É DE 80KM/H, VOCÊ FOI MULTADO EM R${(velocidade-80)*7},00 REAIS!')
else:
    print('PODE SEGUIR, VOCÊ ESTÁ DENTRO DOS LIMITES DA VELOCIDADE!')

