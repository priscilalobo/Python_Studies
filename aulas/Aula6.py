# Trabalhando números como string

numero1 = input('Insira o 1 número')
numero2 = input('Insira o 2 numero')
print('A soma total é', numero1 + numero2)

# Trabalhando numeros como int

numero3 = int(input('Insira o primeiro numero:'))
numero4 = int(input('Insira o segundo numero:'))
print('A some vale', numero3+numero4)

# Forma do professor

numero5 = int(input('Insira o primeiro numero'))
numero6 = int(input('Insira o segundo numero'))
s = numero5+numero6
print('A soma é', s)

# Usando o format

n1 = int(input('Insira o primeiro numero'))
n2 = int(input('Insira o segundo numero'))
s = n1+n2
print(f'A soma é {s}')

# Outra forma

n3 = int(input('Digite o valor'))
n4 = int(input('Digite o valor'))
s = n3+n4
print('A soma de', n3, '+', n4, f'é {s}')
print(f'A soma de {n3} + {n4} é {s}')

# Valor float

n = float(input('Digite um valor'))
print(n)

n10 = bool(input('Digite um valor'))
print(n10)

# se é numerico
n11 = input('Digite algo')
print(n11.isnumeric())