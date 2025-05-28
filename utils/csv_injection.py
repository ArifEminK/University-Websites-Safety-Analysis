import pandas as pd

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# CSV injection riski: CSV hücreleri =, +, - veya @ ile başlıyorsa potansiyel risk
def contains_csv_injection(value):
    if isinstance(value, str) and value.startswith(('=', '+', '-', '@')):
        return True
    return False

df["CSV Injection"] = df.apply(
    lambda row: any(contains_csv_injection(str(val)) for val in row.values),
    axis=1
)

df.to_csv("../outputs/ssl_security_full_analiz_csv_injection.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ CSV Injection analizi tamamlandı.")
