# =========================================================================================================================================== #
# -----------------------------------------------------------Manipulação de Strings---------------------------------------------------------- #
# Crie uma função que receba uma string e retorne um dicionário com a contagem de cada caractere, ignorando espaços e maiúsculas/minúsculas.  #
# =========================================================================================================================================== #

# Variáveis 
texto = "Seja bem vindo nesse perfil"
dicionario = {}
n = 1

# Função para retornar um dicionário com a contagem de cada caractere
def contagem(texto: str):
    t = texto.lower().replace(" ", "")
        
    for i in range(len(t)):
        if t[i] not in dicionario:
            dicionario.update({t[i]: n})
        else:
            valor = dicionario[t[i]]
            dicionario.update({t[i]: valor + 1})
    
    lista = list(dicionario.keys())

    for i in range(len(dicionario)):
        if dicionario[t[i]] <= 1:
            print(f"A letra: {lista[i]} se repete {dicionario[t[i]]} vez")
        else:
            print(f"A letra: {lista[i]} se repete {dicionario[t[i]]} vezes")
           
# Chamando a função de contagem
contagem(texto)

# Mostrando o dicionário após fazer todas as separações e inserções
print(dicionario)



# ================================= #
# Para rodar: python -m Dia_02.main #
# ================================= #