"""
Listas

Listas em Pytohn funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO  e também de podermos colocar QUALQUER tipo de dado.

Listas C/Java: Arrays
   - Possuem tamanho e tipo de dado fixo:
   Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
   será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

 - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
 - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar quqalquer tipo de dado;

As listas em Python são representadas por colchetes> []

#  Podemos facilmente checar se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontri o número 8')

num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#  Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#   Adiconar elementos em lista

#  Para adicionar elementos em listas, utilizamos a função append
print(lista1)
lista1.append(42)
print(lista1)

#  OBS: Com append, nós só podemos adicionar 1 elemento por vez
#  lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca vada elemento da lista como valor adicional à lista
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do índice
#  OBS: Isso não substituiu o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e','e', 'k','', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')


