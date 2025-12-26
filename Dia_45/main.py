# ======================================== #
# -----Design Pattern: Singleton---------- #
# Implemente o padrão Singleton em Python. #
# ======================================== #

class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia

obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()

print(obj1 is obj2)
print(obj2 is obj3)

# ================================= #
# Para rodar: python -m Dia_45.main #
# ================================= #
