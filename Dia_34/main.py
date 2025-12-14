# ===================================================== #
# ---Web scraping básico com requests e BeautifulSoup-- #
# Faça um script que busque o título de uma página web. #
# ===================================================== #

import requests
from bs4 import BeautifulSoup

link = "https://www.python.org"

requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")
titulo = site.find("title")

print(titulo)

# ================================= #
# Para rodar: python -m Dia_34.main #
# ================================= #
