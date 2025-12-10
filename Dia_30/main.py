# ============================================================== #
# ---------------------Expressões Geradoras---------------------- #
# Crie uma expressão geradora que gera números quadrados         #
# de 1 a 1000.                                                    #
# ============================================================== #


quadrados = (n * n for n in range(1, 1001))


for q in quadrados:
    print(q)

# ================================= #
# Para rodar: python -m Dia_30.main #
# ================================= #
