# ==========================================================================   #
# ---------------------------Dicionários e Iteração--------------------------- #
# Dado um dicionário com nomes e idades, retorne o nome da pessoa mais velha.  #
# ============================================================================ #

from libs.estilo import formato


lista_de_pessoas = [
    {"name": "Ana", "age": 28},
    {"name": "Bruno", "age": 45},
    {"name": "Carla", "age": 33},
    {"name": "Daniel", "age": 19},
    {"name": "Eduarda", "age": 52},
    {"name": "Felipe", "age": 25},
    {"name": "Gabriela", "age": 39},
    {"name": "Heitor", "age": 68},
    {"name": "Isabela", "age": 22},
    {"name": "João", "age": 31},
    {"name": "Karina", "age": 41},
    {"name": "Lucas", "age": 27},
    {"name": "Mariana", "age": 35},
    {"name": "Nelson", "age": 72},
    {"name": "Olívia", "age": 20},
    {"name": "Pedro", "age": 48},
    {"name": "Quintino", "age": 55},
    {"name": "Rafaela", "age": 29},
    {"name": "Sérgio", "age": 61},
    {"name": "Tatiana", "age": 37},
    {"name": "Ulisses", "age": 44},
    {"name": "Valentina", "age": 24},
    {"name": "William", "age": 30},
    {"name": "Ximena", "age": 50},
    {"name": "Yasmin", "age": 21},
    {"name": "Zeca", "age": 65},
    {"name": "Beatriz", "age": 36},
    {"name": "Caio", "age": 26},
    {"name": "Diana", "age": 49},
    {"name": "Fábio", "age": 58}
]

def key(e):
    return e['age']

def nome_mais_velho(pessoa):
    pessoa.sort(key=key)
    pessoa.reverse()
    x = pessoa[0].get("name")
    return x


def idade_mais_velho(pessoa):
    pessoa.sort(key=key)
    pessoa.reverse()
    y = pessoa[0].get("age")
    return y

formato(f"A pessoa mais velha é o {nome_mais_velho(lista_de_pessoas)} com {idade_mais_velho(lista_de_pessoas)} anos ")



# ================================= #
# Para rodar: python -m Dia_05.main #
# ================================= #