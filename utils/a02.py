import pandas as pd

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# SSL geçerli değilse A02 = True
df["A02 - Cryptographic Failure"] = df["SSL Geçerli mi?"] == False

df.to_csv("../outputs/ssl_security_full_analiz_a02.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ A02 tamamlandı: ssl_security_full_analiz_a02.csv")
