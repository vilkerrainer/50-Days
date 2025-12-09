# ============================================================== #
# ----------------------Conceito de Iteradores------------------ #
# Crie uma classe iteradora que retorna apenas números pares.    #
# ============================================================== #

class IteradorPares:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.atual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        while self.atual <= self.fim:
            numero = self.atual
            self.atual += 1

            if numero % 2 == 0:
                return numero

        raise StopIteration


pares = IteradorPares(1, 20)

for p in pares:
    print(p)

# ================================= #
# Para rodar: python -m Dia_28.main #
# ================================= #
