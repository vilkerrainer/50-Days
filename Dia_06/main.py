# =================================================================================================================== #
# --------------------------------------------Manipulação de arquivos (txt)------------------------------------------ #
# Crie um script que leia um arquivo texto, conte quantas palavras tem e gere um arquivo resumo com essa informação.  #
# =================================================================================================================== #

import re

with open('Dia_06/texto.txt', 'r', encoding='utf-8') as f:
    texto = f.read()
    
palavras = re.findall(r'\w+', texto)
num_palavras = len(palavras)


with open('Dia_06/result.txt', 'w', encoding='utf-8') as f:
    f.write(f'O arquivo tem {str(num_palavras)} palavras')

# ================================= #
# Para rodar: python -m Dia_06.main #
# ================================= #