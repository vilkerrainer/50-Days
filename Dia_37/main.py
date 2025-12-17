# ====================================================== #
# -------------Listas de prioridades (heapq)------------ #
# Use o módulo heapq para criar uma fila de prioridades. #
# ====================================================== #

import heapq

fila_prioridade = []

heapq.heappush(fila_prioridade, (2, "Estudar Python"))
heapq.heappush(fila_prioridade, (1, "Responder e-mails"))
heapq.heappush(fila_prioridade, (3, "Assistir aula"))
heapq.heappush(fila_prioridade, (1, "Resolver bug urgente"))

while fila_prioridade:
    prioridade, tarefa = heapq.heappop(fila_prioridade)
    print(f"Prioridade {prioridade} -> {tarefa}")


# ================================= #
# Para rodar: python -m Dia_37.main #
# ================================= #
