"""
PEP 8 - Python Enhancement Proposal

São prpostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia de PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nome de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass



[2] - Utilize nomes em minúsculo, separando por underline para as funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - utilize 4 espaços para identação! (NÃO USE TAB)

if 'a' in 'banana':
    print('tem')


[4] - Linhas em branco
-Separar funções e definiçoes de classe com duas linhas em banco;
-Métodos dentro de uma classe devem ser separados com uma única linha em brnaco;


class Classe:
    pass


class Outra:
    pass


[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda - se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem serv colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variveis globais.

[6] - Espaços em expressões e instruções


# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

#Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x             =1
y             =3
variavel_longa=5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""



