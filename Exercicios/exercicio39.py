# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que

from datetime import date
idade = int(input('Em que ano você nasceu? '))
alistamento = date.today().year - idade
print(f'Você tem {alistamento} anos')
if alistamento == 18:
    print('Você precisa se alistar agora!')
elif alistamento < 18:
    print(f'Você ainda tem {18-alistamento} anos para se candidatar')
else:
    print(f'Você deveria ter se candidatado há {alistamento-18} anos atrás')


