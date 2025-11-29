# ===================================================================== #
# ----------------------Manipulação de data e hora--------------------- #
# Calcule a diferença entre duas datas e informe em anos, meses e dias. #
# ===================================================================== #

from datetime import date
from dateutil.relativedelta import relativedelta # type: ignore

def calcular_diferenca_com_dateutil(data_inicio, data_fim):
    if data_inicio > data_fim:
        data_inicio, data_fim = data_fim, data_inicio

    diferenca = relativedelta(data_fim, data_inicio)
    
    return (diferenca.years, diferenca.months, diferenca.days)

# --- Exemplo de uso ---
data_nascimento = date(2005, 11, 19)
data_hoje = date.today() 

anos, meses, dias = calcular_diferenca_com_dateutil(data_nascimento, data_hoje)

print(f"Data de início: {data_nascimento.strftime('%d/%m/%Y')}")
print(f"Data de fim:    {data_hoje.strftime('%d/%m/%Y')}")
print("-" * 30)
print(f"A diferença é de {anos} anos, {meses} meses e {dias} dias.")

# Outro exemplo
data1 = date(2022, 1, 25)
data2 = date(2024, 3, 10)
anos, meses, dias = calcular_diferenca_com_dateutil(data1, data2)
print("\n--- Outro Exemplo ---")
print(f"Data de início: {data1.strftime('%d/%m/%Y')}")
print(f"Data de fim:    {data2.strftime('%d/%m/%Y')}")
print("-" * 30)
print(f"A diferença é de {anos} anos, {meses} meses e {dias} dias.")

# ================================= #
# Para rodar: python -m Dia_19.main #
# ================================= #