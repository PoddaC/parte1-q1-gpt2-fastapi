from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=500, examples=["Once upon a time"])
    max_new_tokens: int = Field(50, ge=5, le=200, description="Qtde. máxima de tokens novos")
    temperature: float = Field(0.8, gt=0.0, le=2.0, description="Maior = mais criativo")


class GenerateResponse(BaseModel):
    prompt: str
    generated_text: str
    model: str
