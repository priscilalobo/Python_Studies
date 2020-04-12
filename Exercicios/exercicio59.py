#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

"""n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero: '))
escolha = 0
while escolha != 5:
    escolha = int(input('Escolha a opção no Menu:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'))
    if escolha == 1:
        print(f'A soma é {n1+n2}')
    elif escolha == 2:
        print(f'O resultado da multiplicação é {n1*n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O número maior é {n1}')
        else:
            print(f'O número maior é {n2}')
    elif escolha == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    else:
        print('Opção inválida, tente novamente!')
print('Finalizando o programa!')"""





#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Escolha o primeiro valor: '))
n2 = int(input('Escolha o segundo valor: '))
opcao = 0
while opcao != 5:
   print('O que você quer fazer? \n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] sair do programa')
   opcao = int(input('Escolha a opção: '))
   if opcao == 1:
    soma = (n1+n2)
    print(f'A soma é {soma} \n=======================')
   elif opcao == 2:
    multiplicar = (n1*n2)
    print(f'A multiplicação é {multiplicar} \n=======================')
   elif opcao == 3:
      if n1 > n2:
        print(f'O número maior é {n1} \n=======================')
      else:
        print(f'O número maior é {n2} \n=======================')
   elif opcao == 4:
    n1 = int(input('Escolha um novo número: '))
    n2 = int(input('Escolha um novo número: '))
   elif opcao ==5:
       print('Você saiu do programa')
   else:
    print('Opçao inválida, digite um1 número de 1 a 5: \n=======================')





















