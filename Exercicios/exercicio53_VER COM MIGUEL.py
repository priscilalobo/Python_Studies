#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#  desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Você digitou a frase {frase}')
palavras = frase.split()
junto = ('').join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso+junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')