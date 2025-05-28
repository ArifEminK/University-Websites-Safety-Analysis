import pandas as pd

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")

# Tüm ek sütunlara ait dosyalar
sutun_dosyalar = {
    # OWASP A01-A10
    "A01 - Broken Access Control": "../outputs/ssl_security_full_analiz_a01.csv",
    "A02 - Cryptographic Failure": "../outputs/ssl_security_full_analiz_a02.csv",
    "A04 - Insecure Design": "../outputs/ssl_security_full_analiz_a04.csv",
    "A05 - Security Misconfiguration": "../outputs/ssl_security_full_analiz_a05.csv",
    "A06 - Vulnerable and Outdated Components": "../outputs/ssl_security_full_analiz_a06.csv",
    "A07 - Identification and Authentication Failures": "../outputs/ssl_security_full_analiz_a07.csv",
    "A09 - Security Logging and Monitoring Failures": "../outputs/ssl_security_full_analiz_a09.csv",
    "A10 - Server-Side Request Forgery": "../outputs/ssl_security_full_analiz_a10.csv",

    # OWASP açığı modülleri
    "CSV Injection": "../outputs/ssl_security_full_analiz_csv_injection.csv",
    "CRLF Injection": "../outputs/ssl_security_full_analiz_crlf.csv",
    "Unrestricted File Upload": "../outputs/ssl_security_full_analiz_upload.csv",

    # HTML/Güvenlik
    "X-Powered-By Exposure": "../outputs/ssl_security_full_analiz_xpowered.csv",
    "Iframe Kullanımı": "../outputs/ssl_security_full_analiz_iframe.csv",
    "Mixed Content Risk": "../outputs/ssl_security_full_analiz_mixedcontent.csv",
    "Deprecated HTML Elements": "../outputs/ssl_security_full_analiz_deprecated.csv",
    "Referrer Policy Mevcut mu?": "../outputs/ssl_security_full_analiz_referrer.csv",

    # Kalite/Performans
    "Gzip Compression Aktif mi?": "../outputs/ssl_security_full_analiz_gzip.csv",
    "robots.txt Var mı?": "../outputs/ssl_security_full_analiz_robots.csv",
    "sitemap.xml Var mı?": "../outputs/ssl_security_full_analiz_sitemap.csv",
    "Doctype Var mı?": "../outputs/ssl_security_full_analiz_doctype.csv",
    "Title Tag Var mı?": "../outputs/ssl_security_full_analiz_title.csv",

    # Son eklenenler
    "Secure/HttpOnly Cookie Flag Eksik?": "../outputs/ssl_security_full_analiz_cookie_flag.csv",
    "HSTS Süresi Yetersiz mi?": "../outputs/ssl_security_full_analiz_hsts.csv",
    "CORS Açıklığı Var mı?": "../outputs/ssl_security_full_analiz_cors.csv",
    "Yanıt Süresi (ms)": "../outputs/ssl_security_full_analiz_response_time.csv",
    "Mobil Uyumlu mu?": "../outputs/ssl_security_full_analiz_mobile.csv",
    "Başlık Boş mu?": "../outputs/ssl_security_full_analiz_title_empty.csv",

    # Son 15 eklenti

    "Tüm IMG'lerde Lazy Load Var mı?": "../outputs/ssl_security_full_analiz_lazy_images.csv",
    "JS Dosya Sayısı": "../outputsssl_security_full_analiz_js_count.csv",
    "Formda Password Input Var mı?": "../outputs/ssl_security_full_analiz_password_input.csv",
    "Toplam HTML Tag Sayısı": "../outputs/ssl_security_full_analiz_tagcount.csv",
    "Tracking Script Var mı?": "../outputs/ssl_security_full_analiz_tracking.csv",
    "HTTPS Yönlendirme Var mı?": "../outputs/ssl_security_full_analiz_https_redirect.csv",
    "Sıkı CSP Var mı?": "../outputs/ssl_security_full_analiz_csp_strict.csv",
    "OG Tag Var mı?": "../outputs/ssl_security_full_analiz_og_tags.csv",
    "Structured Data Var mı?": "../outputs/ssl_security_full_analiz_structured_data.csv",
    "SSL Sertifikası Geçerli mi?": "../outputs/ssl_security_full_analiz_ssl_valid.csv",
    "H1 Etiket Sayısı": "../outputs/ssl_security_full_analiz_h1_count.csv",
    "Inline Script Kullanımı": "../outputs/ssl_security_full_analiz_inline_script.csv",
    "Meta Robots İçeriği": "../outputs/ssl_security_full_analiz_meta_robots.csv",
    "Başlık Uzunluğu (karakter)": "../outputs/ssl_security_full_analiz_title_length.csv",
    "Tüm IMG'lerde loading/width/height var mı?": "../outputs/ssl_security_full_analiz_img_attrs.csv",
}

# Tüm sütunları ana tabloya birleştir
for sutun, dosya in sutun_dosyalar.items():
    try:
        temp = pd.read_csv(dosya, sep=";")
        if sutun in temp.columns:
            df[sutun] = temp[sutun]
            print(f"✅ Eklendi: {sutun}")
        else:
            print(f"⚠️ Sütun bulunamadı: {sutun}")
    except FileNotFoundError:
        print(f"❌ Dosya bulunamadı: {dosya}")

# Final çıktı
output_path = "../outputs/FINAL_FULL_OWASP_ANALIZ.csv"
df.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")
print(f"🎯 Tamamlandı! Final CSV dosyası: {output_path}")
