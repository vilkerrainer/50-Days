# ============================================================== #
# ----------------------Debugging com pdb------------------------ #
# Utilize o debugger para encontrar e corrigir um erro.          #
# ============================================================== #

import pdb


def calcular_media(valores):
    total = 0
    for v in valores:
        total += v
    return total / len(valores)


numeros = []

pdb.set_trace()

media = calcular_media(numeros)
print("Média:", media)

# ================================= #
# Para rodar: python -m Dia_43.main #
# ================================= #
