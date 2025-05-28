import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_title_length(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title
        return len(title.string.strip()) if title and title.string else 0
    except:
        return 0

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Başlık Uzunluğu (karakter)"] = df["İnternet Adresi"].apply(get_title_length)
df.to_csv("../outputs/ssl_security_full_analiz_title_length.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Title uzunluğu sütunu eklendi.")
