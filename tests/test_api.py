from fastapi.testclient import TestClient

from app.main import app
from app.services.generation_service import get_generator


def fake_generator(prompt, **kwargs):
    return [{"generated_text": prompt + " ... continuação simulada"}]


app.dependency_overrides[get_generator] = lambda: fake_generator
client = TestClient(app)



def test_generate_ok():
    r = client.post("/generate", json={"prompt": "Once upon a time"})
    assert r.status_code == 200
    body = r.json()
    assert body["generated_text"].startswith("Once upon a time")
    assert body["model"] == "gpt2"


def test_generate_rejects_empty_prompt():
    assert client.post("/generate", json={"prompt": ""}).status_code == 422


def test_generate_rejects_missing_prompt():
    assert client.post("/generate", json={}).status_code == 422

