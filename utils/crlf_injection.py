import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def has_crlf_injection(domain):
    try:
        domain = domain.replace("http://", "").replace("https://", "").split("/")[0]
        url = "https://" + domain
        r = requests.get(url, timeout=5)
        headers = r.headers
        for k, v in headers.items():
            if '\r' in k or '\n' in k or '\r' in v or '\n' in v:
                return True
        return False
    except:
        return False

df["CRLF Injection"] = df["İnternet Adresi"].apply(has_crlf_injection)

df.to_csv("../outputs/ssl_security_full_analiz_crlf.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ CRLF Injection analizi tamamlandı.")
