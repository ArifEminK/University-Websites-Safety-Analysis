import pandas as pd

# Analiz dosyasını oku
df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# Sadece A01 sütunu ekle veya güncelle
df["A01 - Broken Access Control"] = True

# Yeni CSV olarak kaydet
df.to_csv("outputs/ssl_security_full_analiz_a01.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ A01 sütunu eklendi. Yeni dosya: outputs/ssl_security_full_analiz_a01.csv")
