import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def has_upload_form(domain):
    try:
        domain = domain.replace("http://", "").replace("https://", "").split("/")[0]
        url = "https://" + domain
        r = requests.get(url, timeout=5)
        html = r.text.lower()
        return any(x in html for x in ["type=\"file\"", "enctype=\"multipart/form-data\""])
    except:
        return False

df["Unrestricted File Upload"] = df["İnternet Adresi"].apply(has_upload_form)

df.to_csv("../outputs/ssl_security_full_analiz_upload.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Unrestricted File Upload analizi tamamlandı.")
