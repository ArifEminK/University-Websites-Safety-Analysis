
import pandas as pd
import requests
from bs4 import BeautifulSoup

def check_lazy_images(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        imgs = soup.find_all("img")
        return all(img.get("loading") == "lazy" for img in imgs if img.get("loading")) if imgs else False
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Tüm IMG'lerde Lazy Load Var mı?"] = df["İnternet Adresi"].apply(check_lazy_images)
df.to_csv("../outputs/ssl_security_full_analiz_lazy_images.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Lazy load görsel kontrolü sütunu eklendi.")
