# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 7+1):
    nasc = int(input(f'Qual o ano de nascimento {pessoa}º pessoa? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior+1
    else:
        totmenor = totmenor+1
print(f'Temos {totmaior} pessoas maiores de idade\nTemos {totmenor} pessoas menores de idade')





