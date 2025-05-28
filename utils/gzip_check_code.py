import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def gzip_aktif_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return r.headers.get("Content-Encoding", "").lower() == "gzip"
    except:
        return False

df["Gzip Compression Aktif mi?"] = df["İnternet Adresi"].apply(gzip_aktif_mi)

df.to_csv("../outputs/ssl_security_full_analiz_gzip.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Gzip Compression kontrolü tamamlandı.")