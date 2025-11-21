# ==================================================================================== #
# -----------------------Manipulação de listas multidimensionais---------------------- #
# Crie uma função que receba uma matriz (lista de listas) e retorne a transposta dela. #
# ==================================================================================== #

def transpor_matriz(matriz):
    if not matriz:
        return []

    num_linhas = len(matriz)

    num_colunas = len(matriz[0]) 

    matriz_transposta = []

    for j in range(num_colunas):
        nova_linha = []
        
        for i in range(num_linhas):            
            nova_linha.append(matriz[i][j])     

        matriz_transposta.append(nova_linha)

    return matriz_transposta

minha_matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matriz_resultado = transpor_matriz(minha_matriz)

print("Matriz Original:")
for linha in minha_matriz:
    print(linha)


print("\nMatriz Transposta:")
for linha in matriz_resultado:
    print(linha)

# ================================= #
# Para rodar: python -m Dia_10.main #
# ================================= #