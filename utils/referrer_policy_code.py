import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def referrer_policy_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "referrer-policy" in r.headers
    except:
        return False

df["Referrer Policy Mevcut mu?"] = df["İnternet Adresi"].apply(referrer_policy_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_referrer.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Referrer Policy sütunu eklendi.")