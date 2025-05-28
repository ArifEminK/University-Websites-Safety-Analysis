import pandas as pd
import requests
import re

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def title_bos_mu(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        match = re.search(r"<title>(.*?)</title>", r.text, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip() == ""
        return True
    except:
        return True

df["Başlık Boş mu?"] = df["İnternet Adresi"].apply(title_bos_mu)
df.to_csv("../outputs/ssl_security_full_analiz_title_empty.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Title tag boşluk kontrolü tamamlandı.")