# ============================================================================================================================== #
# ------------------------------------------------------Exceções (try/except)--------------------------------------------------- #
# Faça um programa que receba um número do usuário e trate o erro caso não seja um número válido, pedindo para tentar novamente. #
# ============================================================================================================================== #

from libs.estilo import formato

while True:  
    try:
        n1 = int(input("Digite um número: "))
        formato(f"O número escolhido foi: {n1}")
        break
    except:
        formato("Por favor digite um número")
        

# ================================= #
# Para rodar: python -m Dia_08.main #
# ================================= #