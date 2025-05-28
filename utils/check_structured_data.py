
import pandas as pd
import requests

def has_structured_data(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "application/ld+json" in r.text.lower()
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Structured Data Var mı?"] = df["İnternet Adresi"].apply(has_structured_data)
df.to_csv("../outputs/ssl_security_full_analiz_structured_data.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Structured data sütunu eklendi.")
