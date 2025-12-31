# =========================================================== #
# --------------Manipulação de dados com NumPy--------------- #
# Crie arrays multidimensionais e faça operações matemáticas. #
# =========================================================== #

import numpy as np

matriz_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matriz_b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


soma = matriz_a + matriz_b
subtracao = matriz_b - matriz_a
multiplicacao = matriz_a * matriz_b
media = np.mean(matriz_b)


print("Matriz A:\n", matriz_a)
print("Matriz B:\n", matriz_b)

print("\nSoma:\n", soma)
print("\nSubtração:\n", subtracao)
print("\nMultiplicação:\n", multiplicacao)
print("\nMédia da matriz B:", media)

# ================================= #
# Para rodar: python -m Dia_50.main #
# ================================= #
