#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome santo

cidade = input("Em que cidade você nasceu? ").strip()
print(cidade[:5].lower() == 'santo')
