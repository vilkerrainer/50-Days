# ============================================================================================================================= #
# -------------------------------------------------------Funções e Listas------------------------------------------------------ #
# Escreva uma função que receba uma lista de números e retorne uma nova lista com os números ao quadrado, mas apenas os pares.  #
# ============================================================================================================================= #



# Imports
from libs.estilo import formato
from libs.gerar_lista import gerar_lista

# Variáveis
tamanho_lista = 10
lista = []
n_par = []

# Função para separar os números pares
def par(lista):
    for i in range(len(lista)):
        n = lista[i]
        if (n%2 == 0):
            n_par.append(n)

# Chamando a função para gerar a lista
gerar_lista(tamanho_lista, lista)

# Chamando a função para separar a lista em apenas números pares
par(lista)

# Chamando a função para mostrar a lista
formato(f"Lista: {lista}")

# Chamando a função para mostrar a lista com apenas números pares
formato(f"Lista par: {n_par}")



# ================================= #
# Para rodar: python -m Dia_01.main #
# ================================= #