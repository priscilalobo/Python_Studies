#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

a = float(input('Insira o primeiro seguimento: '))
b = float(input('Insira o primeiro seguimento: '))
c = float(input('Insira o primeiro seguimento: '))

if (abs(b-c) < a) and ((b+c) > a):
    if (abs(a-c) < b) and ((a + c) > b):
        if (abs(a-b) < c) and ((a + b) > c):
            print('Podemos formar um triângulo')
else:
    print('Não podemos formar um triângulo')
