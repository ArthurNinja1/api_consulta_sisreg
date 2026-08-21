from fastapi import FastAPI, HTTPException, Response
from dotenv import load_dotenv, find_dotenv
from consulta import consultar
import json
import os
 
app = FastAPI()

#Carrega o CPF e o nome da mãe do .env
load_dotenv(find_dotenv())
MEU_CPF = os.getenv("MEU_CPF")
NOME_MAE = os.getenv("NOME_MAE")


#Funcção para filtrar os dados do json
def filtrar_solicitacao(item: dict) -> dict:
    fonte = item.get("_source", {})

    procedimentos = [
        p.get("descricao_interna")
        for p in fonte.get("procedimentos", [])
    ]
 
    return {
        "codigo_solicitacao": fonte.get("codigo_solicitacao"),
        "status": fonte.get("status_solicitacao"),
        "procedimentos": procedimentos,
        "cid": fonte.get("descricao_cid_solicitado"),
        "data_solicitacao": fonte.get("data_solicitacao"),
        "data_marcacao": fonte.get("data_marcacao"),
        "unidade_solicitante": fonte.get("nome_unidade_solicitante"),
        "unidade_executante": fonte.get("nome_unidade_executante"),
        "medico_solicitante": fonte.get("nome_medico_solicitante"),
    }

@app.get("/")
async def puxar_dados():
    if not MEU_CPF or not NOME_MAE:
        raise HTTPException(
            status_code=500,
            detail="MEU_CPF ou NOME_MAE não configurados no .env",
        )
    try:
        dados = await consultar(MEU_CPF, NOME_MAE)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Falha na consulta: {e}")

    resultado = [filtrar_solicitacao(item) for item in dados]
    #Formata o resultado para ficar mais legível
    texto_formatado = json.dumps(resultado, indent=4, ensure_ascii=False)
    return Response(content=texto_formatado, media_type="application/json")

