#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

"""nome = str(input('Qual é o seu nome? ')).strip()
print('Muito prazer em te conhecer!')
separa= nome.split()
print(f'Seu primeiro nome é {separa[0]}')
print(f'Seu último nome é {separa[len(separa)-1]}')"""

#outra forma com menos linhas
nome = str(input('Qual é o seu nome completo? ')).strip().split()
print(f'Muito prazer em te conhecer! \nSeu primeiro nome é {nome[0]}\nSeu último nome é {nome[-1]}')





