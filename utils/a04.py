import pandas as pd
import requests

# Ana CSV'yi oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# Insecure design kontrol fonksiyonu
def insecure_design_olasi_mi(url):
    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        full_url = "https://" + domain
        r = requests.get(full_url, timeout=5)
        content = r.text.lower()

        # Giriş varsa ama ek güvenlik öğesi yoksa
        if any(word in content for word in ["login", "password", "signin", "giriş", "şifre"]):
            if not any(word in content for word in ["captcha", "2fa", "two-factor", "security code", "doğrulama", "reset code"]):
                return True
        return False
    except:
        return False

# Uygula
print("🔍 A04 kontrolü başlatıldı...")
df["A04 - Insecure Design"] = df["İnternet Adresi"].apply(insecure_design_olasi_mi)

# Sonuçları yaz
output_path = "../outputs/ssl_security_full_analiz_a04.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"✅ A04 analizi tamamlandı. Kayıt: {output_path}")
