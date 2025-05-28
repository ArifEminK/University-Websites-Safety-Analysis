import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def mobil_uyumlu_mu(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        html = r.text.lower()
        return "viewport" in html and ("bootstrap" in html or "tailwind" in html)
    except:
        return False

df["Mobil Uyumlu mu?"] = df["İnternet Adresi"].apply(mobil_uyumlu_mu)
df.to_csv("../outputs/ssl_security_full_analiz_mobile.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Mobil uyumluluk kontrolü tamamlandı.")