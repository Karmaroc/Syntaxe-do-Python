"""Async e Await

 A função deve ser executada de forma assincrona e o controle de execução será dado a outra corrotina e será retomado quando estiver pronto.
"""

import asyncio

# Async, define uma função como corrotina, permitindo que ela pause sua execução. 
# Await, suspende a execução da corrotina atual até que outra tarefa seja concluída.

async def main():
    print("Inicio")
    await asyncio.sleep(2)
    print("Fim")

asyncio.run(main())

async def fetch_data():
    
    try:
        await asyncio.sleep(1)
        raise ValueError("Erro simulado") # exceção manual
    
    except ValueError as e:
        print(f"Ocorreu um erro: {e}")
        
asyncio.run(fetch_data())


