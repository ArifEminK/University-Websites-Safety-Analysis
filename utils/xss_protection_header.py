import pandas as pd
import requests

def check_x_xss_protection(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return 'x-xss-protection' in r.headers
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["X-XSS-Protection Header Var mı?"] = df["İnternet Adresi"].apply(check_x_xss_protection)
df.to_csv("../outputs/ssl_security_full_analiz_xss.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ X-XSS-Protection Header sütunu eklendi.")
