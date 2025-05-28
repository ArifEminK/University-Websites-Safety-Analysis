from fastapi import FastAPI
from pydantic import BaseModel

# GÜNCELLENECEK: buraya gerçek analiz ve skor fonksiyonlarını koyacağız

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/analyze")
async def analyze(req: URLRequest):
    url = req.url
    result = analyze_url(url)  # analiz et
    score = calculate_score(result)  # skoru hesapla
    return {"score": score, "details": result}
