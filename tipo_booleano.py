"""
Tipo Booleano

Algebra Booleana, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula.

Errado:

true, false

Certo

True, False
"""

ativo = True

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fezendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja sempre o contrário.
"""

print(not ativo)

logado = True


# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores.Ou um ou outro deve ser verdadeiro.

True or True = True
True or False = True
False or True = True
False or Flase = False
"""

print(True or True)

print(ativo or logado)  # ativo = True  # logado = True

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
# exemplos

print(5 > 6)  # False
print(5 < 6)  # True
print(6 == 6)  # True
print(4 <= 5)  # True

num1 = 7
num2 = 8
print(num1 > num2)  # False
print(num1 < num2)  # True
print(num1 == num2)  # False
print(num1 == num1)  # True
print(num2 == num2)  # True

print(num1 < num2 or num1 > 3)   # True
print(num2 > num1 > 3)   # True
print(type(True))
print(type(False))
print(type(ativo))


