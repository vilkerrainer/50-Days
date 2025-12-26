# ================================================ #
# ---------------Loggings avançados--------------- #
# Configure logs com níveis INFO, WARNING e ERROR. #
# ================================================ #

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("MeuLogger")


def dividir(a, b):
    logger.info(f"Tentando dividir {a} por {b}")

    if b == 0:
        logger.error("Erro: tentativa de divisão por zero!")
        return None

    resultado = a / b

    if resultado < 1:
        logger.warning("Resultado muito pequeno!")

    logger.info(f"Resultado calculado: {resultado}")
    return resultado

dividir(10, 2)
dividir(5, 0)
dividir(1, 5)

# ================================= #
# Para rodar: python -m Dia_44.main #
# ================================= #
