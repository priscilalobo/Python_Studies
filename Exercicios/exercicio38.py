#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print(f'O numero maior é {valor1}')
elif valor1 == valor2:
    print('Os números são iguais')
else:
    print(f'O valor maior é o {valor2}')

