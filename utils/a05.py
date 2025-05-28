import pandas as pd

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

df["A05 - Security Misconfiguration"] = (
    (df["X-Frame-Options"] == False) |
    (df["X-Content-Type-Options"] == False)
)

df.to_csv("../outputs/ssl_security_full_analiz_a05.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ A05 tamamlandı: ssl_security_full_analiz_a05.csv")
