# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra  A aparece {frase.count("A")} vezes')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1} ')
print (f'A ultima posição que apareceu a letra A foi {frase.rfind("A")+1}')



