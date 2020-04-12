n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Ele é numérico?', n.isnumeric())
print('Ele é letra?', n.isalpha())
print('Ele está em minúsculo?', n.islower())
print('Ele está em maiscúlo?', n.isupper())
print(f'Ele está capitalizado? {n.istitle()}')
print(f'Ele é alphanúmerico? {n.isalnum()}')

