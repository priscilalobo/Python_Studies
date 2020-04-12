# Crie um programa que considere quanto de dinheiro a pessoa tem na carteira e mostre
# quantos dólares ela pode comprar USD1,00 = R$3,81
x = float(input('Quanto você tem na carteira? R$'))
print(f'Com R${x} você consegue comprar {x/3.81:.2f} dólares e {x/4.28:.2f} euros')
