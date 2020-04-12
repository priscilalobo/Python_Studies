# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
n = int(input('Digite um valor: '))
cm = n*100
mm = n*1000
km = n/1000
print(f'{n} metros é igual a {cm} centímetros\n{n} metros é igual a {mm} milímetros\n{n} metros é igual a {km} km')
