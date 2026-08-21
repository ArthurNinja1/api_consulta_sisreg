Sistema para extrair dados do SISREG pela API do Portal Transparência.

Arquivos
 \consulta.py — função de consulta à API.
 \main.py — API FastAPI que expõe os dados.

Variáveis necessárias
- MEU_CPF
- NOME_MAE

Pode definir manualmente em consulta.py:
    MEU_CPF="seu_cpf"
    NOME_MAE="nome_da_mae"

Ou criar um .env:
    MEU_CPF="seu_cpf"
    NOME_MAE="nome_da_mae"

para rodar:
    pip install fastapi uvicorn httpx python-dotenv
    uvicorn main:app --reload

Acesse http://localhost:8000/.