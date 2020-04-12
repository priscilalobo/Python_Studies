#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Entre 5.0 e 6.9: recuperação
# - igual ou maior 7.0: aprovado

nota1 = float(input('Digite a nota do 1 semestre: '))
nota2 = float(input('Digite a nota do 2 semestre: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('Você foi reprovado')
elif media >= 7.0:
    print('Você passou de ano')
else:
    print('Você está de recuperação')
