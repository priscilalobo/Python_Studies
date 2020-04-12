# Crie um algorítimo que leia um número e mostre seu dobro, triplo e raiz quadrada
n = int(input('Digite um valor: '))
d = n*2
t = n*3
r = n**(1/2)
print(f'O seu dobro é {d}\nO triplo é {t}\nA raiz quadrada é {r:.2f}')

# Outra forma sem variavéis
n1 = int(input('Digite um valor: '))
print(f'O dobro de {n1} é igual a {n1*2}\nO triplo de {n1} é igual a {n1*3}\nA raiz quadrada de {n1} é igual a {n1**(1/2):.2f}')

