# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60,00 por dia e R$0,15 por km rodado.

d = float(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km você rodou com o carro?' ))
pago = (d*60)+(km*0.15)
print(f'O total a pagar por {d} dias rodados e {km} km rodados é de R${pago}')
