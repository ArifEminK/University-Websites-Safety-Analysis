import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def title_tag_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "<title>" in r.text.lower()
    except:
        return False

df["Title Tag Var mı?"] = df["İnternet Adresi"].apply(title_tag_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_title.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Title tag kontrolü tamamlandı.")