import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def has_x_powered_by(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return 'x-powered-by' in r.headers
    except:
        return False

df["X-Powered-By Exposure"] = df["İnternet Adresi"].apply(has_x_powered_by)

df.to_csv("../outputs/ssl_security_full_analiz_xpowered.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ X-Powered-By Exposure sütunu eklendi.")