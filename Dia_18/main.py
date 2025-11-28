# ================================================================================================ #
# ----------------------------------------------JSON---------------------------------------------- #
# Crie um script que leia um arquivo JSON com dados de usuários e filtre só os maiores de 18 anos. #
# ================================================================================================ #

import json

with open('Dia_18/pessoas.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

maior_idade = []
menor_idade = []

for pessoa in dados:
    nome = pessoa["nome"]
    idade = pessoa["idade"]
    if idade >= 18:
        maior_idade.append({"Nome": nome, "Idade": idade})
    else:
        menor_idade.append({"Nome": nome, "Idade": idade})


print("\n"+"="*177)
print(f"\nPessoas com mais de 18 anos ou com 18: {maior_idade}\n")
print(f"\nPessoas com menos de 18 anos: {menor_idade}\n")
print("="*177)

# ================================= #
# Para rodar: python -m Dia_18.main #
# ================================= #