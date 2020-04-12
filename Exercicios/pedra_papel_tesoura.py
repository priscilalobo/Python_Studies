from random import randint

player = input('Faça sua escolha:') # pedra, papel, tesoura
escolhas = ['pedra','papel','tesoura']
pc = escolhas[randint(0,2)]

if player.lower() == pc:
    print(f'Player: {player.lower()} x Pc: {pc} -> empate')
elif player.lower() == 'pedra' and pc == 'papel':
    print(f'Player: {player.lower()} x Pc: {pc} -> você perdeu')
elif player.lower() == 'papel' and pc == 'tesoura':
    print(f'Player: {player} x Pc: {pc} -> você perdeu')
elif player.lower() == 'tesoura' and pc == 'pedra':
    print(f'Player: {player} x Pc: {pc} -> você perdeu')
elif player.lower() == 'pedra' and pc == 'tesoura':
    print(f'Player: {player} x Pc: {pc} -> você ganhou')
elif player.lower() == 'papel' and pc == 'pedra':
    print(f'Player: {player} x Pc: {pc} -> você ganhou')
elif player.lower() == 'tesoura' and pc == 'papel':
    print(f'Player: {player} x Pc: {pc} -> você ganhou')
else:
    print('você digitou errado')