# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
# porção inteira

import math
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e seu número inteiro é {math.trunc(n)}')

from math import trunc
n1 = float(input('Digite um valor: '))
print(f'O valor digitado foi {n1} e sua porção inteira é {trunc(n1)}')

# Também dá pra usar: print(f'O valor digitado foi {n1} e sua porção inteira é {int(n1)}')




