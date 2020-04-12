# Sorteando uma ordem na lista: nome de 4 alunos e o programa vai definir a ordem de apresentação

from random import shuffle

pa = str(input('Nome do primeiro aluno: '))
sa = str(input('Nome do segundo aluno: '))
ta = str(input('Nome do terceiro aluno: '))
qa = str(input('Nome do quarto aluno: '))
lista = [pa,sa,ta,qa]
shuffle(lista)
print('A ordem da apresentação do trabalho será: ')
print(lista)

from random import sample
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
lista1 = [n1,n2,n3]
ordem = sample(lista1, k=2)
print(f'{ordem}')