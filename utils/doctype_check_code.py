import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def doctype_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "<!doctype html" in r.text.lower()
    except:
        return False

df["Doctype Var mı?"] = df["İnternet Adresi"].apply(doctype_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_doctype.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Doctype kontrolü tamamlandı.")