# ================================================================= #
# --------------------------Recursão simples----------------------- #
# Escreva uma função recursiva que calcule o fatorial de um número. #
# ================================================================= #

n = 5

def fatorial(n):

    a = 1
    nums = []

    for i in range(n):
        nums.append(n)
        n = n - 1

    for i in range(len(nums)):
        a = a * nums[i]

    return a

print(f"O resultado é: {fatorial(n)}")

# ================================= #
# Para rodar: python -m Dia_12.main #
# ================================= #