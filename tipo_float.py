"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais  na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla

valor = 1, 44
print(valor)
print(type(valor))

#  Certo do ponto de vista Float

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer a dupla atribuição

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(type(5j))
print(variavel **2)

# Exemplo-01
salario1 = 2.56
salario2 = 3.67
print(f'Total {salario1 + salario2}')

# Exemplo-02
res = int(salario1 + salario2)
print(res)
print(f'Total {res}')
print(type(res))