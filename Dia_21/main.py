# ============================================================================ #
# ----------------------------Geradores (generators)-------------------------- #
# Crie um gerador que gere os números da sequência de Fibonacci até um limite. #
# ============================================================================ #

def gerador_fibonacci(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

limite_maximo = 100

print(f"Gerando a sequência de Fibonacci até {limite_maximo}:")

fib_gen = gerador_fibonacci(limite_maximo)

for numero in fib_gen:
    print(numero, end=" ")

# ================================= #
# Para rodar: python -m Dia_21.main #
# ================================= #