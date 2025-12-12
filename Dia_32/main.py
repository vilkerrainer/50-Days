# ============================================================ #
# -----------------Processos com multiprocessing-------------- #
# Calcule a soma de grandes listas usando múltiplos processos. #
# ============================================================ #

import multiprocessing as mp


def soma_parcial(numeros):
    return sum(numeros)

if __name__ == "__main__":
    lista_grande = list(range(1, 10_000_001))

    num_processos = mp.cpu_count()

    tamanho_parte = len(lista_grande) // num_processos
    partes = [
        lista_grande[i * tamanho_parte : (i + 1) * tamanho_parte]
        for i in range(num_processos)
    ]

    with mp.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_parcial, partes)

    soma_total = sum(resultados)

    print(f"Soma total: {soma_total}")

# ================================= #
# Para rodar: python -m Dia_32.main #
# ================================= #
