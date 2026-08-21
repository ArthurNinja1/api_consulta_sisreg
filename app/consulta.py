import httpx
 
URL = "https://sisreg-transparencia.treslagoas.ms.gov.br"
 
 
async def consultar(cpf: str, nome_mae: str) -> dict:
    async with httpx.AsyncClient() as client:
        resposta = await client.get(
            f"{URL}/api/consulta/{cpf}",
            params={"nome_mae": nome_mae},
        )
        resposta.raise_for_status()
        return resposta.json()
