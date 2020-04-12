# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você irá pagar?'))
emprestimo = valor / (ano*12)
autorizacao = salario * 0.30
print(f'O valor da prestação será {emprestimo}')
if emprestimo <= autorizacao:
    print(f'Emprestimo autorizado')
else:
    print('Emprestimo não autorizado')


