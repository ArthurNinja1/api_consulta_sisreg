import asyncio
import httpx
import json
import os
from dotenv import load_dotenv, find_dotenv

URL = "https://sisreg-transparencia.treslagoas.ms.gov.br"

load_dotenv(find_dotenv())
MEU_CPF = os.getenv("MEU_CPF")
NOME_MAE = os.getenv("NOME_MAE")


async def consultar(cpf, nome_mae):
    async with httpx.AsyncClient() as client:
        resposta = await client.get(
            f"{URL}/api/consulta/{cpf}",
            params={"nome_mae": nome_mae}
        )

        print("Status:", resposta.status_code)

        dados = resposta.json()
        
        print("Resposta:")
        print(json.dumps(
            dados,
            indent=4,
            ensure_ascii=False
        ))

asyncio.run(
    consultar(
        MEU_CPF,
        NOME_MAE
    )
)

