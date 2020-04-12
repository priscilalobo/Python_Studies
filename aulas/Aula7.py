n1 = int(input('Digite o valor'))
n2 = int(input('Digite o segundo valor'))
s = n1+n2
d = n1/n2
m = n1*n2
e = n1**n2
di = n1//n2
sobra = n1%n2
print(f'A soma é {s}\n a divisão é {d:.3f}', end=' ')
print(f'a multiplicação é {m}, a exponenciação é {e}\na divisão inteira é {di} e a sobra é {sobra}')
