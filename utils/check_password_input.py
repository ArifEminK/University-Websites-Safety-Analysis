
import pandas as pd
import requests
from bs4 import BeautifulSoup

def has_password_input(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return any(input.get("type") == "password" for input in soup.find_all("input"))
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["Formda Password Input Var mı?"] = df["İnternet Adresi"].apply(has_password_input)
df.to_csv("../outputs/ssl_security_full_analiz_password_input.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Password input sütunu eklendi.")
