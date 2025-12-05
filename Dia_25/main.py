# ============================================================== #
# -------------Listas ligadas (implementação simples)----------- #
# Implemente uma lista ligada simples com inserir e remover.     #
# ============================================================== #

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    def remover(self, valor):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def exibir(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Lista vazia"


lista = ListaLigada()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)

print("Lista após inserções:", lista.exibir())

lista.remover(20)
print("Lista após remover 20:", lista.exibir())

lista.remover(30)
print("Lista após remover 30:", lista.exibir())

# ================================= #
# Para rodar: python -m Dia_25.main #
# ================================= #
