# essa aula, vamos aprender como utilizar estruturas condicionais simples
# e compostas nos seus programas em Python.

idade = int(input('Quantos anos você tem? '))
if idade >=28:
    print('Você está velho')
else:
    print('Você está novo')
print('--FIM--')

nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'PRISCILA':
    print('Que nome lindo você tem!')
else:
    print('Você não é quem eu estava procurando!')
print(f'Bom dia {nome.capitalize()}!')
