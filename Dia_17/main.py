# ============================================================================ #
# ----------------------Manipulação avançada de strings----------------------- #
# Faça uma função que receba um texto e retorne a palavra mais frequente nele. #
# ============================================================================ #

import string
from collections import Counter

def encontrar_palavra_mais_frequente(texto):
    if not isinstance(texto, str) or not texto.strip():
        return None

    stopwords_pt = {
        'a', 'o', 'e', 'é', 'de', 'do', 'da', 'dos', 'das', 'em', 'um', 'uma',
        'uns', 'umas', 'para', 'com', 'não', 'os', 'as', 'ao', 'aos', 'à', 'às',
        'pelo', 'pela', 'pelos', 'pelas', 'que', 'se', 'mas', 'ou', 'como',
        'seu', 'sua', 'seus', 'suas', 'foi', 'for', 'ser', 'são', 'tem', 'ter',
        'nos', 'no', 'na', 'nas', 'por', 'sem', 'sim', 'essa', 'esse', 'isso'
    }

    tabela_pontuacao = str.maketrans('', '', string.punctuation + '“”¡¿')
    texto_limpo = texto.lower().translate(tabela_pontuacao)

    palavras = texto_limpo.split()

    palavras_filtradas = [p for p in palavras if p not in stopwords_pt]

    if not palavras_filtradas:
        return None

    contagem = Counter(palavras_filtradas)
    palavra_mais_comum, _ = contagem.most_common(1)[0]

    return palavra_mais_comum

texto_exemplo = """
A persistência é o caminho do êxito. Sim, o caminho!
Muitas vezes, a diferença entre o sucesso e o fracasso não é a força ou o conhecimento,
mas sim a persistência. Acreditar e persistir, essa é a chave.
"""

palavra = encontrar_palavra_mais_frequente(texto_exemplo)
print(f"A palavra mais frequente é: '{palavra}'")

texto_exemplo_2 = "Um dois dois três três três quatro quatro quatro quatro."
palavra_2 = encontrar_palavra_mais_frequente(texto_exemplo_2)
print(f"A palavra mais frequente é: '{palavra_2}'")

texto_stopwords = "O rato roeu a roupa do rei de roma, e a rainha."
palavra_3 = encontrar_palavra_mais_frequente(texto_stopwords)
print(f"A palavra mais frequente é: '{palavra_3}'")

texto_vazio = "   "
palavra_4 = encontrar_palavra_mais_frequente(texto_vazio)
print(f"Resultado para texto vazio: {palavra_4}")

# ================================= #
# Para rodar: python -m Dia_17.main #
# ================================= #