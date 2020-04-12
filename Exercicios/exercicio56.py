# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

media = 0
nomevelho = 0
maioridade = 0
count = 0
mulher = 0
for pessoa in range(1,5):
    print(f'---{pessoa}º PESSOA---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media = count/4
    count = count+idade
    if sexo in 'Ff' and idade < 20:
       mulher = mulher+1
    if pessoa == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nomevelho
print(f'Temos {mulher} menores que 20 anos')
print(f'A idade media das pessoas é {media}')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {maioridade}')

