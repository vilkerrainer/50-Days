# ================================================================= #
# -----------------Listas e filtragem com filter()----------------- #
# Use filter() para retornar apenas os números primos de uma lista. #
# ================================================================= #

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def is_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
            
    return True

numeros_primos_iterador = filter(is_primo, lista)

lista_de_primos = list(numeros_primos_iterador)

print(f"Lista original: {lista}")
print(f"Números primos encontrados: {lista_de_primos}")

# ================================= #
# Para rodar: python -m Dia_13.main #
# ================================= #