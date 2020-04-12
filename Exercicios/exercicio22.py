#analisando o texto

n = str(input('Qual é o seu nome? ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiusculo é {n.upper()}')
print(f'Seu nome em minusculo é {n.lower()}')
separa = n.split(' ')
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')

print(f"Seu nome tem ao todo {len(n) - n.count(' ')} letras")
#ou
print(f"Seu nome tem ao todo {len(n.replace(' ',''))} letras")


