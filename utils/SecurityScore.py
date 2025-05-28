import pandas as pd

df = pd.read_csv("../outputs/FINAL_FULL_OWASP_ANALIZ.csv", sep=";", encoding="utf-8-sig")

# 1. OWASP başlıkları (kapsananlar)
owasp_cols = [
    "A01 - Broken Access Control",
    "A02 - Cryptographic Failure",
    "A04 - Insecure Design",
    "A05 - Security Misconfiguration",
    "A06 - Vulnerable and Outdated Components",
    "A07 - Identification and Authentication Failures",
    "A09 - Security Logging and Monitoring Failures",
    "A10 - Server-Side Request Forgery"
]

# 2. HTTPS & SSL & HSTS kriterleri
crypto_cols = [
    "HTTPS Yönlendirme Var mı?",
    "SSL Sertifikası Geçerli mi?",
    "HSTS Süresi Yetersiz mi?"  # burada TRUE kötü, bu yüzden tersine çevrilecek
]

# 3. Header Güvenliği
header_cols = [
    "Sıkı CSP Var mı?",
    "CORS Açıklığı Var mı?",       # TRUE kötü, ters
    "X-XSS-Protection Header Var mı?",
    "Secure/HttpOnly Cookie Flag Eksik?"  # TRUE kötü, ters
]

# 4. HTML riskleri
html_risk_cols = [
    "X-Powered-By Exposure",   # TRUE kötü
    "Iframe Kullanımı",        # TRUE kötü
    "Mixed Content Risk"       # TRUE kötü
]

# 5. Diğer
other_cols = [
    "Tracking Script Var mı?",    # TRUE kötü
    "Unrestricted File Upload",   # TRUE kötü
]

# Skor hesaplaması
def calculate_score(row):
    score = 0

    # OWASP: her biri 5 puan (8 tanesi)
    score += sum([1 for col in owasp_cols if row.get(col) == True]) * (40 / len(owasp_cols))

    # HTTPS/SSL: her biri 1/3 ağırlıklı
    if row.get("HTTPS Yönlendirme Var mı?") == True:
        score += 20 / 3
    if row.get("SSL Sertifikası Geçerli mi?") == True:
        score += 20 / 3
    if row.get("HSTS Süresi Yetersiz mi?") == False:  # iyi olan False
        score += 20 / 3

    # Header güvenliği (4 madde, her biri 3.75 puan)
    score += 3.75 if row.get("Sıkı CSP Var mı?") == True else 0
    score += 3.75 if row.get("X-XSS-Protection Header Var mı?") == True else 0
    score += 3.75 if row.get("CORS Açıklığı Var mı?") == False else 0
    score += 3.75 if row.get("Secure/HttpOnly Cookie Flag Eksik?") == False else 0

    # HTML riskleri (her biri 3.33 puan, negatifse ceza)
    score += 3.33 * (3 - sum([1 for col in html_risk_cols if row.get(col) == True]))

    # Diğer (her biri 2.5 puan, negatifse ceza)
    score += 2.5 * (2 - sum([1 for col in other_cols if row.get(col) == True]))

    return round(score, 2)

# Skoru hesapla
df["Güvenlik Skoru (%)"] = df.apply(calculate_score, axis=1)

# Yeni dosyayı kaydet
output_path = "../outputs/FINAL_WITH_SECURITY_SCORE.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")

output_path
