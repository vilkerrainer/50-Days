# ==================================================================================== #
# -------------------------------------Threading básico------------------------------- #
# Faça um programa que rode duas tarefas em threads diferentes (ex: contador e timer). #
# ==================================================================================== #

import threading
import time


def contador():
    for i in range(1, 11):
        print(f"[CONTADOR] Número: {i}")
        time.sleep(0.5)


def timer():
    for i in range(5):
        print(f"[TIMER] Passou 1 segundo ({i+1}/5)")
        time.sleep(1)


thread1 = threading.Thread(target=contador)
thread2 = threading.Thread(target=timer)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Execução finalizada.")

# ================================= #
# Para rodar: python -m Dia_31.main #
# ================================= #
