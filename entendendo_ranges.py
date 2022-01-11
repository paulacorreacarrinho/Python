"""

Ranges

- Precisamos conhecer o loop for para usar os ranges.
-Precisamos conhecer o range para treabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de formar aleatória,
mais sim de maneira especificada.

Formas gerais:]

#Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive(início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

#Forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Formula 2
for num in range(1, 11):
    print(num)


#Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Formula 4
for num in range(10, 0, -1):
    print(num)

"""
