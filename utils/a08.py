import pandas as pd

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

df["A08 - Software/Data Integrity Failure"] = (
    (df["Strict-Transport-Security"] == False) |
    (df["Content-Security-Policy"] == False)
)

df.to_csv("../outputs/ssl_security_full_analiz_a08.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ A08 tamamlandı: ssl_security_full_analiz_a08.csv")
