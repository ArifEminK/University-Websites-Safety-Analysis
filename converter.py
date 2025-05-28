import pandas as pd

df = pd.read_csv("outputs/FINAL_FULL_OWASP_ANALIZ.csv", sep=";")

# Sadece bool olan sütunları seç
bool_cols = [col for col in df.columns if df[col].dropna().isin([True, False]).all()]

# TRUE -> 1, FALSE -> 0
for col in bool_cols:
    df[col] = df[col].astype(int)

# Yeni sütun: Toplam Güvenlik Skoru
df["Toplam Skor"] = df[bool_cols].sum(axis=1)

# Kaydet
df.to_csv("FINAL_WITH_SCORE.csv", sep=";", index=False, encoding="utf-8-sig")
