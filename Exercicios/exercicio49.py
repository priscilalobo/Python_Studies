# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

print('TABUADA')
escolha = int(input('Informe o número da tabuada que você quer: '))
for n in range(0,11):
    print(f'{escolha}x{n}={escolha*n}')
