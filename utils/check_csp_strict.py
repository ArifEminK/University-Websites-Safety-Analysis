
import pandas as pd
import requests

def check_strict_csp(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        csp = r.headers.get("content-security-policy", "").lower()
        return "'self'" in csp and "default-src" in csp
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Sıkı CSP Var mı?"] = df["İnternet Adresi"].apply(check_strict_csp)
df.to_csv("../outputs/ssl_security_full_analiz_csp_strict.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Sıkı CSP sütunu eklendi.")
