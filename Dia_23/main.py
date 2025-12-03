# ============================================================= #
# ----------------Programação Funcional: reduce()-------------- #
# Use reduce() para calcular o produto de uma lista de números. #
# ============================================================= #

from functools import reduce

numeros = [2, 3, 4]
produto = reduce(lambda x, y: x * y, numeros)
print(f"resultado: {produto}")

# ================================= #
# Para rodar: python -m Dia_23.main #
# ================================= #