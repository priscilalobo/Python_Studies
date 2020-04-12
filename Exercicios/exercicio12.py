""""
faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

"""
x = float(input('Qual o valor do produto? R$'))
desc = x*0.05
valor = x-desc
print(f'Você pagou R${x}, mas com o desconto de 5% saiu por {valor}')

# Outra forma
y = float(input('Qual o valor do produto? R$'))
descy = y-(y*10 / 100)
print(f'Você pagou {y}, mas com desconto ficou {descy}')


