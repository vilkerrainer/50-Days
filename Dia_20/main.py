# =============================================================================== #
# -----------------------------------Decoradores--------------------------------- #
# Implemente um decorador que registre o tempo que uma função leva para executar. #
# =============================================================================== #

import time
import functools

def medir_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        
        resultado = func(*args, **kwargs)
        
        fim = time.perf_counter()
        
        tempo_decorrido = fim - inicio
        print(f"A função '{func.__name__}' levou {tempo_decorrido:.4f} segundos para executar.")
        
        return resultado
        
    return wrapper


@medir_tempo
def funcao_lenta():
    time.sleep(1)
    print("Função lenta finalizada.")

@medir_tempo
def calculo_rapido(n):
    soma = sum(i**2 for i in range(n))
    return soma


print("\nExecutando a função que não recebe argumentos e não retorna valor:")
funcao_lenta()

print("Executando a função que recebe um argumento e retorna um valor:")
resultado_calculo = calculo_rapido(100000)
print(f"O resultado do cálculo foi: {resultado_calculo}\n")

# ================================= #
# Para rodar: python -m Dia_20.main #
# ================================= #