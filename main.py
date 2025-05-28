from utils.analiz import kontrol_ssl, kontrol_security_headers, hesapla_owasp_ve_skor
import pandas as pd

# Veriyi oku
df = pd.read_excel("data/liste.xlsx", header=1)
df = df[["BİRİM ADI", "İNTERNET ADRESİ"]].dropna()

sonuclar = []

print(f"🔍 Toplam {len(df)} üniversite analiz ediliyor...")

for i, row in df.iterrows():
    birim = row["BİRİM ADI"]
    adres = row["İNTERNET ADRESİ"]

    print(f"{i+1}. {birim} ({adres})")

    ssl_info = kontrol_ssl(adres)
    headers = kontrol_security_headers(adres)
    owasp_risks, skor = hesapla_owasp_ve_skor(ssl_info, headers)

    sonuc = {
        "Birim Adı": birim,
        "İnternet Adresi": adres,
        "HTTPS Var mı?": ssl_info["https_var"],
        "SSL Geçerli mi?": ssl_info["ssl_gecerli"],
        "Sertifika Başlangıç": ssl_info["not_before"],
        "Sertifika Bitiş": ssl_info["not_after"],
        **headers,
        **owasp_risks,
        "Güvenlik Skoru (0-5)": skor
    }

    sonuclar.append(sonuc)

# Sonuçları kaydet
df_sonuc = pd.DataFrame(sonuclar)
df_sonuc.to_csv("outputs/ssl_security_full_analiz.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ Tüm analiz tamamlandı → outputs/ssl_security_full_analiz.csv")
