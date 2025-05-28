
import pandas as pd
import requests

def has_og_tags(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        return "property=\"og:" in r.text.lower()
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["OG Tag Var mı?"] = df["İnternet Adresi"].apply(has_og_tags)
df.to_csv("../outputs/ssl_security_full_analiz_og_tags.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ OpenGraph tag sütunu eklendi.")
