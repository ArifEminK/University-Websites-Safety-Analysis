
import pandas as pd
import requests

def check_https_redirect(domain):
    try:
        http_url = "http://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(http_url, timeout=5, allow_redirects=True)
        return r.url.startswith("https://")
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["HTTPS Yönlendirme Var mı?"] = df["İnternet Adresi"].apply(check_https_redirect)
df.to_csv("../outputs/ssl_security_full_analiz_https_redirect.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ HTTPS yönlendirme sütunu eklendi.")
