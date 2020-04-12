#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num = int(input('Digite um numero: '))
count = 0
for c in range(1, num+1):
    if num % c == 0:
     print('\033[33m', end='')
     count = count + 1
    else:
     print('\033[31m', end='')
    print(c, end=' ')
print(f'O número {num} é divisivel {count} vezes')
if count == 2:
    print('E por isso ele é primo')
else:
    print('Ele não é primo')


