# Parte 1 – Questão 1: Geração de texto com GPT-2 (FastAPI)

API que recebe uma frase em JSON, usa o **GPT-2** (HuggingFace `transformers`) para gerar uma continuação e devolve o resultado em JSON.

## Estrutura
```
app/
  main.py                         # cria o app, lifespan (carrega o modelo no startup) e registra routers
  routers/generation.py           # POST /generate
  services/generation_service.py  # carga do GPT-2 (CPU/GPU) e dependência get_generator
  models/generation.py            # schemas Pydantic de entrada/saída
tests/test_api.py                 # testes com o modelo substituído por um fake
```

## Como executar
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Na primeira requisição o modelo (~500 MB) é baixado do HuggingFace Hub e mantido em memória.

Documentação interativa: <http://127.0.0.1:8000/docs>

## Exemplo
```bash
curl -X POST http://127.0.0.1:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Once upon a time", "max_new_tokens": 40}'
```
Resposta:
```json
{"prompt": "Once upon a time", "generated_text": "Once upon a time, ...", "model": "gpt2"}
```
Parâmetros opcionais: `max_new_tokens` (5–200, padrão 50) e `temperature` (0–2, padrão 0.8).

## Testes
```bash
python -m pytest -q
```
Os testes não baixam o modelo (usam `dependency_overrides`).
