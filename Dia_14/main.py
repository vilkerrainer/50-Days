# ========================================================================================== #
# -------------------------------Criar um dicionário invertido------------------------------ #
# Dado um dicionário com chave-valor, crie outro onde os valores são as chaves e vice-versa. #
# ========================================================================================== #

dados_pessoas = {
    "nome1": "Ana",
    "idade1": 25,
    "nome2": "Bruno",
    "idade2": 32,
    "nome3": "Carla",
    "idade3": 19,
    "nome4": "Daniel",
    "idade4": 45
}

dados_invertidos = {valor: chave for chave, valor in dados_pessoas.items()}

print("Dicionário Original:")
print(dados_pessoas)

print("\n" + "-"*30 + "\n") 

print("Dicionário Invertido:")
print(dados_invertidos)

# ================================= #
# Para rodar: python -m Dia_14.main #
# ================================= #