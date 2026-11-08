from fastapi import APIRouter, Depends

from app.models.generation import GenerateRequest, GenerateResponse
from app.services.generation_service import MODEL_NAME, get_generator

router = APIRouter(tags=["geração"])


@router.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest, generator=Depends(get_generator)) -> GenerateResponse:
    # `def` (síncrono): o FastAPI executa em threadpool e não bloqueia o event loop.
    outputs = generator(
        req.prompt,
        max_new_tokens=req.max_new_tokens,
        do_sample=True,
        temperature=req.temperature,
        num_return_sequences=1,
        pad_token_id=50256,  # eos do GPT-2; evita warning
    )
    return GenerateResponse(prompt=req.prompt, generated_text=outputs[0]["generated_text"], model=MODEL_NAME)
