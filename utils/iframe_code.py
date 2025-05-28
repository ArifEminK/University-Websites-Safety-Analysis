import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def iframe_kullanim_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "iframe" in r.text.lower()
    except:
        return False

df["Iframe Kullanımı"] = df["İnternet Adresi"].apply(iframe_kullanim_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_iframe.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Iframe Kullanımı sütunu eklendi.")