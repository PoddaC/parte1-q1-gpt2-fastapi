"""Camada de serviço: carrega o GPT-2 uma única vez e o expõe como dependência."""
from functools import lru_cache
from typing import Callable

MODEL_NAME = "gpt2"

def get_device() -> int:
    """0 = primeira GPU (se houver CUDA); -1 = CPU."""
    import torch

    return 0 if torch.cuda.is_available() else -1


@lru_cache(maxsize=1)
def get_generator() -> Callable:
    # Import tardio: os testes não precisam do torch/transformers.
    from transformers import pipeline

    return pipeline("text-generation", model=MODEL_NAME, device=get_device())
