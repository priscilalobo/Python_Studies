# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15%
# de aumento

s = float(input('Qual o salário do funcionário? R$'))
r = s+(s*15/100)
print(f'Um funcionário que ganhava R${s}, com 15% de aumento, passa a receber R${r}')
