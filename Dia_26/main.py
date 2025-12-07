# ============================================================== #
# --------------------Manipulação de CSV------------------------ #
# Leia um arquivo CSV e calcule a média de uma coluna numérica.  #
# ============================================================== #

import csv

def calcular_media_csv(arquivo, coluna):
    valores = []

    with open(arquivo, 'r', newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)

        if coluna not in leitor.fieldnames:
            print(f"Coluna '{coluna}' não encontrada no arquivo.")
            return None

        for linha in leitor:
            try:
                valor = float(linha[coluna])
                valores.append(valor)
            except ValueError:
                # Ignora valores não numéricos
                pass

    if not valores:
        print("Nenhum valor numérico encontrado na coluna.")
        return None

    return sum(valores) / len(valores)


# ======================== EXEMPLO DE USO ======================= #
media = calcular_media_csv("Dia_26/dados.csv", "salario")

if media is not None:
    print(f"Média da coluna 'salario': {media:.2f}")

# ================================= #
# Para rodar: python -m Dia_26.main #
# ================================= #
