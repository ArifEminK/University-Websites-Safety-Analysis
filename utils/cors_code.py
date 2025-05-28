import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def cors_acik_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        cors = r.headers.get("Access-Control-Allow-Origin", "")
        return "*" in cors
    except:
        return False

df["CORS Açıklığı Var mı?"] = df["İnternet Adresi"].apply(cors_acik_mi)
df.to_csv("../outputs/ssl_security_full_analiz_cors.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ CORS açığı kontrolü tamamlandı.")