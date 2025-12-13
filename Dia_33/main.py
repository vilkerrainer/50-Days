# ================================================================================= #
# -----------------------Funções Async/Await (Asyncio básico)---------------------- #
# Crie uma função assíncrona que aguarde 2 segundos antes de imprimir uma mensagem. #
# ================================================================================= #

import asyncio


async def mensagem_com_atraso():
    await asyncio.sleep(2)
    print("Mensagem exibida após 2 segundos!")


async def main():
    await mensagem_com_atraso()


asyncio.run(main())

# ================================= #
# Para rodar: python -m Dia_33.main #
# ================================= #
