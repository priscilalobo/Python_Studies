#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = resp = media = soma = quant = 0
while (resp != 'n'.upper()):
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    quant +=1
    soma += n
    media = soma / quant
    if maior < n:
        maior = n
    else:
        menor = n
    if resp != 's'.upper() and resp != 'n'.upper():
        print('Erro, tente novamente com S ou N')

print(f'A média dos números foi {media}, o maior número foi {maior} e o menor número foi {menor}')



#Comentário youtube
"""maior = menor = media = s = c = p =  0
while(p != "s".upper()):
        num = int(input("Digite um número: "))
        p = str(input("Deseja parar?[S/N]")).upper().strip()
        c+= 1
        s += num
        media = s / c
        if(maior < num):
             maior = num
        else:
            menor = num
        if(p != "n".upper() and p != "s".upper()):
            print("Erro, tente novamente!")
print("A média dos números digitados: {}" .format(media))
print("Maior número: {}" .format(maior))
print("Menor número: {}" .format(menor))"""

#Forma que o professor fez

