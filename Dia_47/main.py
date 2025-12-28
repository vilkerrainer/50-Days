# ===================================================================== #
# ------------------------------Metaclasses---------------------------- #
# Introdução simples a metaclasses, alterando comportamento de classes. #
# ===================================================================== #

class MinhaMeta(type):
    def __new__(cls, nome, bases, atributos):
        print(f"Classe '{nome}' está sendo criada pela metaclasse!")
        atributos["criado_por_metaclasse"] = True
        return super().__new__(cls, nome, bases, atributos)


class Pessoa(metaclass=MinhaMeta):
    def __init__(self, nome):
        self.nome = nome
        
p = Pessoa("Carlos")

print("Nome:", p.nome)
print("Criado por metaclasse:", p.criado_por_metaclasse)

# ================================= #
# Para rodar: python -m Dia_47.main #
# ================================= #
