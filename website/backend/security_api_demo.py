#uvicorn security_api_demo:app --reload
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import ssl, socket
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

def analyze_url(url):
    domain = url.replace("http://", "").replace("https://", "").split("/")[0]
    base_url = "https://" + domain
    results = {}

    # HTTPS yönlendirme
    try:
        r = requests.get("http://" + domain, timeout=5, allow_redirects=True)
        results["HTTPS Yönlendirme Var mı?"] = r.url.startswith("https://")
    except:
        results["HTTPS Yönlendirme Var mı?"] = False

    # SSL sertifikası
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                results["SSL Sertifikası Geçerli mi?"] = True
    except:
        results["SSL Sertifikası Geçerli mi?"] = False

    # HSTS Süresi Yetersiz mi? = False olması iyi
    results["HSTS Süresi Yetersiz mi?"] = False  # örnek olarak varsayalım (geliştirilebilir)

    # HTML üzerinden: img lazy, script inline
    try:
        r = requests.get(base_url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        imgs = soup.find_all("img")
        results["Tüm IMG'lerde Lazy Load Var mı?"] = all(img.get("loading") == "lazy" for img in imgs if img.has_attr("loading"))
        results["Inline Script Kullanımı"] = any(script.string is not None for script in soup.find_all("script"))
    except:
        results["Tüm IMG'lerde Lazy Load Var mı?"] = False
        results["Inline Script Kullanımı"] = True

    # Rastgele diğer metrikler (örnek)
    results["X-Powered-By Exposure"] = False
    results["Iframe Kullanımı"] = False
    results["Tracking Script Var mı?"] = False
    results["Mixed Content Risk"] = False
    results["Sıkı CSP Var mı?"] = True
    results["CORS Açıklığı Var mı?"] = False
    results["Secure/HttpOnly Cookie Flag Eksik?"] = False

    return results

def calculate_score(results):
    score = 0

    # OWASP örneği: 8 başlık simülasyonu (elde yok, örnek üzerinden)
    owasp_total = 8
    score += (6 / owasp_total) * 40  # örnek: 6 tanesi TRUE

    # HTTPS & SSL & HSTS
    score += 20 / 3 if results.get("HTTPS Yönlendirme Var mı?") else 0
    score += 20 / 3 if results.get("SSL Sertifikası Geçerli mi?") else 0
    score += 20 / 3 if not results.get("HSTS Süresi Yetersiz mi?") else 0

    # Header güvenliği
    score += 3.75 if results.get("Sıkı CSP Var mı?") else 0
    score += 3.75 if not results.get("CORS Açıklığı Var mı?") else 0
    score += 3.75 if not results.get("Secure/HttpOnly Cookie Flag Eksik?") else 0

    # HTML riskleri
    html_risks = [
        ("X-Powered-By Exposure", False),
        ("Iframe Kullanımı", False)
    ]
    score += 3.33 * sum(1 for k, desired in html_risks if results.get(k) == desired)

    # Diğer
    other = [
        ("Tracking Script Var mı?", False),
        ("Mixed Content Risk", False)
    ]
    score += 2.5 * sum(1 for k, desired in other if results.get(k) == desired)

    # Inline script cezalı
    if not results.get("Inline Script Kullanımı"):
        score += 2.5

    return round(score, 2)

@app.post("/analyze")
async def analyze(req: URLRequest):
    data = analyze_url(req.url)
    score = calculate_score(data)
    return {"score": score, "details": data}
