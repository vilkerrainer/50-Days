# ============================================================== #
# -------------Manipulação de arquivos JSON (CRUD)-------------- #
# Crie um CRUD simples usando um arquivo JSON como "banco".      #
# ============================================================== #

import json
import os


ARQUIVO = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


# ---------------------------- CRUD ----------------------------- #

def criar(item):
    dados = carregar_dados()
    dados.append(item)
    salvar_dados(dados)
    print("Item criado com sucesso!")


def ler():
    dados = carregar_dados()
    return dados


def atualizar(indice, novo_item):
    dados = carregar_dados()

    if 0 <= indice < len(dados):
        dados[indice] = novo_item
        salvar_dados(dados)
        print("Item atualizado!")
    else:
        print("Índice inválido.")


def deletar(indice):
    dados = carregar_dados()

    if 0 <= indice < len(dados):
        removido = dados.pop(indice)
        salvar_dados(dados)
        print(f"Item removido: {removido}")
    else:
        print("Índice inválido.")

criar({"nome": "Ana", "idade": 30})
criar({"nome": "João", "idade": 25})

print("Dados atuais:", ler())

atualizar(1, {"nome": "João Silva", "idade": 26})

deletar(0)

print("Dados finais:", ler())

# ================================= #
# Para rodar: python -m Dia_29.main #
# ================================= #
