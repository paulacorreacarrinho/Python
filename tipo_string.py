"""
Tipo string

Em Python um dado é considerado do tipo string sempre que:

 - Estriver entre àspas simples -> 'uma sting', '234', 'a', 'True', '42.3'
 - Estriver entre àspas duplas  -> "uma sting", "234", "a", "True", "42.3"
 - Estriver entre àspas simples triplas -> '''uma sting''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Paula'
print(nome)
print(type(nome))

nome = "Gina's \nBar"  # \n -> serve pra pular uma linha
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"  # \" -> caractere de escape
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper()) #imprime tudo maiúsculo

nome = 'Geek University'
print(nome.lower()) #imprime tudo minúscolo

nome = 'Geek University'
print(nome.title()) #imprime somente com a primeira Letra maiúscula

nome = 'Geek University'
print(nome.split()) #transforma em uma lista de strings

nome = 'Geek University'

print(nome.replace('G', 'P'))  # replace -> pra subistituar uma letra por outra
 """
# Estriver entre àspas duplas triplas -> """uma sting""", """234""", """a""", """True""", """42.3"""

# ['0 ,  1 ,  2 ,  3,   4 ,  5 ,  6 ,  7 ,  8 ,  9 ,  10, 11 , 12 , 13 , 14 ] -
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y'] - converte em uma lista de sting

nome = 'Geek University'
print(nome[0:15])  # Slice de string
print(nome[0:4])   # Slice de string
print(nome[5:15])  # Slice de string

nome = 'Geek University'

# [   0  ,      1      ]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
[::-1] -> Comedo do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1])    # Inversão da string Pythônico
print(nome.replace('e', 'i'))
print(type(nome))

nome = 'Geek University'
nome = nome.split()
print(f'{nome[1]} {nome[0]}') # Inversão da posição da string


texto = 'socorram me subino onibus em marrocos'  # Palíndromo
# Palíndromo ->  pode ler, indiferentemente, da esquerda para a direita ou vice-versa
print(texto)
print(texto[::-1])

nome = 'ana'  # Palíndromo
print(nome)
print(nome[::-1])
