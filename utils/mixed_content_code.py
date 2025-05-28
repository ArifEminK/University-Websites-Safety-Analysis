import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def mixed_content_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        html = r.text.lower()
        return 'src="http://' in html or 'href="http://' in html
    except:
        return False

df["Mixed Content Risk"] = df["İnternet Adresi"].apply(mixed_content_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_mixedcontent.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Mixed Content Risk sütunu eklendi.")