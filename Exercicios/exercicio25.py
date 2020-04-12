# Procurando uma string dentro de outra

nome = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem silva? {"SILVA" in nome.upper().split()}')