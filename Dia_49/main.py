# ====================================================================== #
# --------------------Análise de desempenho com timeit------------------ #
# Compare duas formas de resolver um problema e veja qual é mais rápida. #
# ====================================================================== #

import timeit


def soma_loop():
    total = 0
    for i in range(1_000_000):
        total += i
    return total


def soma_builtin():
    return sum(range(1_000_000))

tempo_loop = timeit.timeit(soma_loop, number=100)
tempo_builtin = timeit.timeit(soma_builtin, number=100)

print(f"Tempo usando loop manual: {tempo_loop:.4f} segundos")
print(f"Tempo usando sum(): {tempo_builtin:.4f} segundos")

# ================================= #
# Para rodar: python -m Dia_49.main #
# ================================= #
