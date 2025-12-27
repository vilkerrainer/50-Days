# ================================================== #
# ------------Expressões Regulares Avançadas-------- #
# Capture grupos específicos em uma string complexa. #
# ================================================== #

import re

def extrair_dados(texto):
    padrao = r"Nome:\s*(\w+)\s*\|\s*Idade:\s*(\d+)\s*\|\s*Email:\s*([\w\.-]+@[\w\.-]+\.\w+)"

    resultado = re.search(padrao, texto)

    if resultado:
        nome = resultado.group(1)
        idade = int(resultado.group(2))
        email = resultado.group(3)
        return nome, idade, email
    return None

texto = "Nome: Carlos | Idade: 28 | Email: carlos@email.com"

dados = extrair_dados(texto)

if dados:
    print(f"Nome: {dados[0]}")
    print(f"Idade: {dados[1]}")
    print(f"Email: {dados[2]}")

# ================================= #
# Para rodar: python -m Dia_46.main #
# ================================= #