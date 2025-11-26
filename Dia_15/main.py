# ========================================================================================== #
# -------------------------------Criar um dicionário invertido------------------------------ #
# Dado um dicionário com chave-valor, crie outro onde os valores são as chaves e vice-versa. #
# ========================================================================================== #

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self._saldo = float(saldo_inicial)
        print(f"Conta de {self.titular} criada com saldo de R$ {self._saldo:.2f}.")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return False
            
        if valor > self._saldo:
            print(f"Erro: Saldo insuficiente. Você tentou sacar R$ {valor:.2f}, mas seu saldo é de R$ {self._saldo:.2f}.")
            return False
        
        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}.")
        return True

    def consultar_saldo(self):
        print(f"O saldo atual da conta de {self.titular} é R$ {self._saldo:.2f}.")
        return self._saldo

    def __str__(self):
        return f"Conta [Titular: {self.titular}, Saldo: R$ {self._saldo:.2f}]"



print("--- Bem-vindo ao Banco Virtual ---")

conta_joao = ContaBancaria("João Silva", 1500.00)
conta_maria = ContaBancaria("Maria Souza")

print("\n--- Operações na Conta de João ---")
conta_joao.consultar_saldo()
conta_joao.depositar(500.50)
conta_joao.sacar(300)
print(conta_joao)

print("\n--- Operações na Conta de Maria ---")
conta_maria.consultar_saldo()
conta_maria.depositar(980.75)
conta_maria.sacar(1200)
conta_maria.sacar(200)
print(conta_maria)

print("\n--- Testando Casos de Erro ---")
conta_joao.depositar(-100)
conta_joao.sacar(-50)


# ================================= #
# Para rodar: python -m Dia_15.main #
# ================================= #