"""
Recebendo dados do usuário

input() ->  Todo dado recebido via input é do tipo string

Em Python, strign é tudo que estiver entre aspas:
-Aspas simples;
-Aspas duplas;
-Aspas simples triplas;
-Aspas duplas triplas.
"""
#  Entrada de dados
# print("Qual o seu nome? ")
# nome = input()  # Input -> entrada

nome = input("Qual o seu nome?")

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
# print(f'Seja bem vindo(a){nome.title()}')  DESTA FORMA {nome.title()} terei o retorno
# do nome somente com a 1ª letra Maiuscula

print(f'Seja bem vindo(a){nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade?'))


#  Processamento

#  Saída de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7

# print(f'A {nome.title()} tem {idade} anos') -> DESTA FORMA {nome.title()} terei o retorno
# do NOME somente com a 1ª letra Maiuscula

print(f'A {nome} tem {idade} anos')

"""

# int(idade+) => cast

Cast é a 'coversão' de um tipo de dado para o outro.
"""
# (f'A {nome.title()} nasceu em {2021 - int(idade)}') - retorno somente com a 1ª letra Maiuscula

print(f'A {nome} nasceu em {2021 - int(idade)}')