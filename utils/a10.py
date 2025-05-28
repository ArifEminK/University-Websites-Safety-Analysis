import pandas as pd

# Ana CSV dosyasını oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# A10 sütununu ekle
print("📌 A10 (SSRF) sütunu 'Kapsam Dışı' olarak ekleniyor...")
df["A10 - Server-Side Request Forgery"] = "Kapsam Dışı"

# Yeni CSV olarak kaydet
output_path = "../outputs/ssl_security_full_analiz_a10.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"✅ A10 tamamlandı. Kayıt: {output_path}")
