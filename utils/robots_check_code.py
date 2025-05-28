import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def robots_txt_var_mi(domain):
    try:
        base = domain.replace("http://", "").replace("https://", "").split("/")[0]
        url = f"https://{base}/robots.txt"
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

df["robots.txt Var mı?"] = df["İnternet Adresi"].apply(robots_txt_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_robots.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ robots.txt kontrolü tamamlandı.")