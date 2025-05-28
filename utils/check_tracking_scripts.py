
import pandas as pd
import requests

def has_tracking_scripts(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        text = r.text.lower()
        return any(x in text for x in ["fbq(", "hotjar", "yandex.metrika"])
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Tracking Script Var mı?"] = df["İnternet Adresi"].apply(has_tracking_scripts)
df.to_csv("../outputs/ssl_security_full_analiz_tracking.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Tracking script sütunu eklendi.")
