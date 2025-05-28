import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def cookie_flag_eksik_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        cookies = r.headers.get("Set-Cookie", "")
        return not ("httponly" in cookies.lower() and "secure" in cookies.lower())
    except:
        return False

df["Secure/HttpOnly Cookie Flag Eksik?"] = df["İnternet Adresi"].apply(cookie_flag_eksik_mi)
df.to_csv("../outputs/ssl_security_full_analiz_cookie_flag.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Cookie flag kontrolü tamamlandı.")