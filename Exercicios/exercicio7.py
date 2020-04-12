# Desenvolva um programa que leias as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Insira a nota do 1 semestre: '))
n2 = float(input('Insira a nota do 2 semestre: '))
m = (n1+n2)/2
print(f'A média aritimetica entre {n1} e {n2} é igual a {m:.2f}')

# Outra forma sem variáveis
n3 = float(input('Insira a nota do 1 semestre: '))
n4 = float(input('Insira a nota do 2 semestre: '))
print(f'A média aritimetica entre {n3} e {n4} é igual a {(n3+n4)/2:.2f}')

