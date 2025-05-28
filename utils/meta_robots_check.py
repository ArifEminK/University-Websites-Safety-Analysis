import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_meta_robots_content(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.find("meta", attrs={"name": "robots"})
        return tag.get("content") if tag else ""
    except:
        return ""

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Meta Robots İçeriği"] = df["İnternet Adresi"].apply(get_meta_robots_content)
df.to_csv("../outputs/ssl_security_full_analiz_meta_robots.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Meta Robots sütunu eklendi.")
