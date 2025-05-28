import pandas as pd
import requests
from bs4 import BeautifulSoup

def has_inline_scripts(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return any(script.string is not None for script in soup.find_all("script"))
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Inline Script Kullanımı"] = df["İnternet Adresi"].apply(has_inline_scripts)
df.to_csv("../outputs/ssl_security_full_analiz_inline_script.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Inline Script Kullanımı sütunu eklendi.")
