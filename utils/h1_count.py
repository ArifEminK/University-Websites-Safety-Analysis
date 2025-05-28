import pandas as pd
import requests
from bs4 import BeautifulSoup

def count_h1_tags(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return len(soup.find_all("h1"))
    except:
        return 0

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["H1 Etiket Sayısı"] = df["İnternet Adresi"].apply(count_h1_tags)
df.to_csv("../outputs/ssl_security_full_analiz_h1_count.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ H1 sayısı sütunu eklendi.")
