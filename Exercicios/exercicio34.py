# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
if salario >= 1250:
    print(f'Seu novo salário é {(salario*0.10)+salario}')
else:
    print(f'Seu novo salário é {(salario*0.15)+salario}')