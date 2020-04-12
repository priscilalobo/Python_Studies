#faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Informe um valor: '))
n = str(num) #não esquecer de passar o numero para string
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

#separa = split.n()
