#vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else
# em programas Python.

nome = str(input('Qual o seu nome? '))
if nome == 'Priscila':
    print('Seu nome é maravilhoso!')
elif nome == 'Miguel' or nome == 'Lourdes' or nome == 'Cintia':
    print('Também acho seu nome lindo!')
elif nome in 'Ana, Guilherme':
    print('Nome estranho!')
else:
    print('Nome comum!')
print(f'Bom dia {nome}')
