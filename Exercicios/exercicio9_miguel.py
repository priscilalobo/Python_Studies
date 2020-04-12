#Outra forma de fazer tabuada usando o FOR
n = int(input('Digite qual tabuada você quer: '))

for x in range(1,11):
    escrever = f"{x}x{n} = {x*n}"
    print(escrever)

# Outra forma de fazer usando List Comprehension
p = int(input('Digite qual tabuada você quer: '))
x = [print(f'{x}x{p} = {x*p}') for x in range(1,11)]

