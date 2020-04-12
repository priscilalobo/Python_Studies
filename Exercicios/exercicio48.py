
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0
count = 0
for cont in range(1, 500, 2):
    if cont%3 == 0:
        soma = soma+cont
        count = count+1
print(f'A soma é {soma} e a contagem é {count}')




'''print(f'A soma dos {len(cont)} números é {sum(cont)} ')'''


"""
ini = 1
fim = 500
int = 1

soma= 0
count= 0
for n in range(ini, fim+1, int):
    if n%3 == 0:
        soma = soma + n
        count = count + 1
print(f"A soma de todos os números de {ini} até {fim} divisíveis por 3 é : {soma}")
print(f"total de números divisiveis por três: {count}")
"""