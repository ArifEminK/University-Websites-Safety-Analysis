import pandas as pd

# Ana CSV dosyasını oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# A09 sütununu ekle (hepsine True)
print("🔍 A09 (Security Logging and Monitoring Failures) işaretleniyor...")
df["A09 - Security Logging and Monitoring Failures"] = True

# Yeni dosyaya kaydet
output_path = "../outputs/ssl_security_full_analiz_a09.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"✅ A09 tamamlandı. Kayıt: {output_path}")
