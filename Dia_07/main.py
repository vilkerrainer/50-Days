# ============================================================================================ #
# ------------------------------------Funções Lambda + sorted--------------------------------- #
# Ordene uma lista de tuplas (nome, idade) pelo segundo elemento (idade) usando função lambda. #
# ============================================================================================ #

lista_de_pessoas = [('Carlos', 30), ('Ana', 25), ('Bruno', 35), ('Zoe', 22)]

lista_ordenada_por_idade = sorted(lista_de_pessoas, key=lambda item: item[1])

print(lista_ordenada_por_idade)
# ================================= #
# Para rodar: python -m Dia_07.main #
# ================================= #