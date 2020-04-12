Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello, world!')
Hello, world!
>>> 5+7
12
>>> print('Olá, mundo!')
Olá, mundo!
>>> print(Olá, mundo!)
SyntaxError: invalid syntax
>>> print(6+3)
9
>>> print('7=4')
7=4
>>> print('7','4')
7 4
>>> print('7'+'4')
74
>>> print('Eu tenho', 27 'anos')
SyntaxError: invalid syntax
>>> print('Eu tenho', 27, 'anos')
Eu tenho 27 anos
>>> print('Eu tenho 27 anos')
Eu tenho 27 anos
>>> nome=priscila
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    nome=priscila
NameError: name 'priscila' is not defined
>>> nome="Priscila'
SyntaxError: EOL while scanning string literal
>>> nome='Priscila'
>>> idade='27'
>>> peso='52 kg'
>>> print('nome, idade, peso')
nome, idade, peso
>>> nome = 'Priscila'
>>> idade = '27'
>>> peso = '52'
>>> print('nome, idade, peso')
nome, idade, peso
>>> print(nome, idade, peso)
Priscila 27 52
>>> nome = input ('Qual é o seu nome')
Qual é o seu nome
>>> nome = input('Qual é o seu nome?)
	     
SyntaxError: EOL while scanning string literal
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome? Priscila
>>> Cidade = ('Qual cidade você mora?')
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome? Priscila
>>> Cidade = input ('Qual cidade você mora?')
Qual cidade você mora? Taubaté
>>> idade = input ('Quantos anos você tem?')
Quantos anos você tem? 27
>>> print(nome, Cidade, idade)
 Priscila  Taubaté  27
>>> 
