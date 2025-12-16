# ===================================================== #
# -------Pandas: Manipulação básica de DataFrames------ #
# Leia um CSV e filtre linhas com base em uma condição. #
# ===================================================== #

import pandas as pd

def filtrar_csv(arquivo, coluna, valor_minimo):
    df = pd.read_csv(arquivo)

    if coluna not in df.columns:
        print(f"Coluna '{coluna}' não encontrada.")
        return None

    filtrado = df[df[coluna] >= valor_minimo]
    return filtrado

resultado = filtrar_csv("Dia_36/dados.csv", "salario", 3000)

if resultado is not None:
    print(resultado)

# ================================= #
# Para rodar: python -m Dia_36.main #
# ================================= #
