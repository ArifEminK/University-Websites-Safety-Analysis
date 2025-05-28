import pandas as pd
import requests

# Ana CSV dosyasını oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# A07 kontrol fonksiyonu
def authentication_zayif_mi(url):
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        full_url = "https://" + domain
        r = requests.get(full_url, timeout=5)
        html = r.text.lower()

        # Şifre/giriş alanı varsa ama ek güvenlik öğesi yoksa
        if any(word in html for word in ["login", "signin", "şifre", "giriş", "password"]):
            if not any(word in html for word in ["captcha", "2fa", "two-factor", "reset code", "security code"]):
                return True
        return False
    except:
        return False

# A07 sütununu hesapla
print("🔍 A07 kontrolü başlatıldı...")
df["A07 - Identification and Authentication Failures"] = df["İnternet Adresi"].apply(authentication_zayif_mi)

# Yeni dosya olarak kaydet
output_path = "../outputs/ssl_security_full_analiz_a07.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"✅ A07 analizi tamamlandı. Kayıt: {output_path}")
