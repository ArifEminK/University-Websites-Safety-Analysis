import pandas as pd
import requests

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

def sitemap_xml_var_mi(domain):
    try:
        base = domain.replace("http://", "").replace("https://", "").split("/")[0]
        url = f"https://{base}/sitemap.xml"
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

df["sitemap.xml Var mı?"] = df["İnternet Adresi"].apply(sitemap_xml_var_mi)

df.to_csv("../outputs/ssl_security_full_analiz_sitemap.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ sitemap.xml kontrolü tamamlandı.")