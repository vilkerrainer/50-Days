# ==================================================================================== #
# ------------------------Uso básico de módulos (math, datetime)---------------------- #
# Escreva uma função que calcule o número de dias entre duas datas dadas pelo usuário. #
# ==================================================================================== #

from datetime import datetime

def calcular_dias_entre_datas():
    
    formato_data = "%d/%m/%Y"
    
    while True:
        data_inicial_str = input("Digite a primeira data (no formato DD/MM/AAAA): ")
        try:
            data_inicial = datetime.strptime(data_inicial_str, formato_data)
            break
        except ValueError:
            print("Formato de data inválido. Por favor, tente novamente.")

    while True:
        data_final_str = input("Digite a segunda data (no formato DD/MM/AAAA): ")
        try:
            data_final = datetime.strptime(data_final_str, formato_data)
            break
        except ValueError:
            print("Formato de data inválido. Por favor, tente novamente.")

    diferenca = data_final - data_inicial

    numero_de_dias = abs(diferenca.days)

    print(f"\nO número de dias entre {data_inicial_str} e {data_final_str} é: {numero_de_dias} dias.")


calcular_dias_entre_datas()

# ================================= #
# Para rodar: python -m Dia_11.main #
# ================================= #