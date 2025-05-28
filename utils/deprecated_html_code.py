import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def deprecated_html_var_mi(domain):
    try:
        url = "https://" + domain.replace("http://", "").replace("https://", "").split("/")[0]
        r = requests.get(url, timeout=5)
        html = r.text.lower()
        eski_tagler = ["<font", "<center", "<marquee", "<bgsound", "<blink"]
        return any(tag in html for tag in eski_tagler)
    except:
        return False

df["Deprecated HTML Elements"] = df["İnternet Adresi"].apply(deprecated_html_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_deprecated.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Deprecated HTML Elements sütunu eklendi.")