# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.




'''sexo = str(input('Qual o seu sexo? responda com F/M: ')).upper().strip()
while sexo != 'F' and sexo !='M':
    sexo = str(input('Digite somente F ou M!')).upper().strip()
print(f'O seu sexo é {sexo}')'''

#outra forma

"""sexo = str(input('Qual o seu sexo? responda com F/M: ')).upper().strip()
while sexo not in 'FfMm':
    sexo = str(input('Digite somente F ou M!')).upper().strip()
print(f'O seu sexo é {sexo}')"""


sexo = str(input('Qual é o seu sexo? Responda com F ou M: ')).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Você só pode digitar F ou M, tente novamente')).upper().strip()[0]
print(f'Você é do sexo {sexo}')

