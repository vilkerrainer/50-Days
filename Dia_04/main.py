# =================================================================================================================== #
# ----------------------------------------Funções com parâmetros padrão e args--------------------------------------- #
# Faça uma função que receba qualquer quantidade de números e retorne a média deles. Se não receber nada, retorne 0.  #
# =================================================================================================================== #

# Imports
from libs.estilo import formato

# Variáveis iniciais
n1 = int(input("Digite quantos númeors deseja adicionar: "))
n2 = 0

# Função central para fazer as médias
def medias(n1, n2):
    lista = []

    # Decisão para saber o que retornar
    if (n1 == 0):
        return 0
    else:
        # Looping para adicionar números na lista
        for i in range(1, n1 + 1):
            n3 = int(input(f"Digite seu {i}º número: "))
            lista.append(n3)
        
        # Looping para gerar uma variável com a soma de todos números da lista
        for m in range(n1):
            n2 = n2 + lista[m]
        
        # Cálculo de média
        media = n2 / n1
        return f"A média de {lista} é {media:.2f}"


# Chamando a função
formato(medias(n1, n2))

# ================================= #
# Para rodar: python -m Dia_04.main #
# ================================= #