# WHILE

'''c = 1
while c < 10+1:
    print(c)
    c = c + 1
print('fim')'''

"""c = 1
while c < 10:
    print (c)
    c = c + 1
print('fim')"""

"""n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')"""

"""r = 'S'
while r == 'S':
    n = input('Digite um valor: ')
    r = input('Quer continuar S/N? ').upper()
print('Fim')"""

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!=0:
        if n % 2 ==0:
            par = par+1
        else:
            impar = impar+1

if impar != 0 and par != 0:
    print(f'Você digitou {par} números pares e {impar} números impares')
else:
    print('Você digitou 0')




