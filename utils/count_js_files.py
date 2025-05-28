
import pandas as pd
import requests
from bs4 import BeautifulSoup

def count_js_files(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return len(soup.find_all("script", src=True))
    except:
        return 0

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["JS Dosya Sayısı"] = df["İnternet Adresi"].apply(count_js_files)
df.to_csv("../outputs/ssl_security_full_analiz_js_count.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ JS dosya sayısı sütunu eklendi.")
