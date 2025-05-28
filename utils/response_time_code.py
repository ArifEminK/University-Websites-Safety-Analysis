import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def yanit_suresi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return round(r.elapsed.total_seconds() * 1000)
    except:
        return -1  # hata varsa -1

df["Yanıt Süresi (ms)"] = df["İnternet Adresi"].apply(yanit_suresi)
df.to_csv("../outputs/ssl_security_full_analiz_response_time.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Yanıt süresi kontrolü tamamlandı.")