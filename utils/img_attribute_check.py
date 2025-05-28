import pandas as pd
import requests
from bs4 import BeautifulSoup

def img_attributes_check(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        imgs = soup.find_all("img")
        return all(img.get("loading") and img.get("width") and img.get("height") for img in imgs) if imgs else False
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Tüm IMG'lerde loading/width/height var mı?"] = df["İnternet Adresi"].apply(img_attributes_check)
df.to_csv("../outputs/ssl_security_full_analiz_img_attrs.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ IMG etiketleri kontrolü sütunu eklendi.")
