# ============================================================== #
# ---------------Múltiplas heranças e Mixins-------------------- #
# Demonstre múltipla herança e como resolver conflitos.          #
# ============================================================== #

class LogMixin:
    def log(self, mensagem):
        print(f"[LOG]: {mensagem}")


class Animal:
    def falar(self):
        return "Som genérico de animal"


class Terrestre:
    def mover(self):
        return "Andando sobre a terra"


class Aquatico:    
    def mover(self):
        return "Nadando na água"


class Sapo(Animal, Terrestre, Aquatico, LogMixin):
    
    def falar(self):
        return "Coaxando"

    def mover(self):
        acao = super().mover()
        self.log(f"Sapo está se movendo: {acao}")
        return acao

sapo = Sapo()

print("Som:", sapo.falar())                     
print("Movimento:", sapo.mover())                
print("MRO:", Sapo.__mro__)                      

# ================================= #
# Para rodar: python -m Dia_27.main #
# ================================= #
