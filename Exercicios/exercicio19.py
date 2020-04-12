# Sorteando um item na lista

import random

pa = input('Digite o nome do primeiro aluno: ')
sa = input('Digite o nome do segundo aluno: ')
ta = input('Digite o nome do terceiro aluno: ')
lista = [pa, sa, ta]
print(f'O aluno escolhido foi {random.choice(lista)}')
