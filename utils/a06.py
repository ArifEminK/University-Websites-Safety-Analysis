import pandas as pd
import requests
import re

# Dosyayı oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# Eski JS/CSS kütüphanelerini tarayan fonksiyon
def eski_component_var_mi(url):
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        full_url = "https://" + domain
        r = requests.get(full_url, timeout=5)
        html = r.text.lower()

        # Aranacak eski kütüphane desenleri
        eski_kutuphaneler = [
            r"jquery\-1\.[0-9]+",
            r"bootstrap\-3\.[0-9]+",
            r"angular\-1\.[0-9]+",
            r"vue(\.js)?\-1\.[0-9]+",
            r"knockout\-2\.[0-9]+"
        ]

        for pattern in eski_kutuphaneler:
            if re.search(pattern, html):
                return True
        return False
    except:
        return False

# A06 sütununu ekle
print("🔍 A06 kontrolü başlatıldı...")
df["A06 - Vulnerable and Outdated Components"] = df["İnternet Adresi"].apply(eski_component_var_mi)

# Sonuçları kaydet
output_path = "../outputs/ssl_security_full_analiz_a06.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"✅ A06 analizi tamamlandı. Kayıt: {output_path}")
