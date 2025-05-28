import pandas as pd
import requests
import re

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def hsts_yetersiz_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        hsts = r.headers.get("Strict-Transport-Security", "")
        match = re.search(r"max-age=(\\d+)", hsts)
        if match:
            return int(match.group(1)) < 31536000
        return True
    except:
        return True

df["HSTS Süresi Yetersiz mi?"] = df["İnternet Adresi"].apply(hsts_yetersiz_mi)
df.to_csv("../outputs/ssl_security_full_analiz_hsts.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ HSTS max-age kontrolü tamamlandı.")