
import pandas as pd
import ssl
import socket

def check_ssl_validity(domain):
    try:
        host = domain.replace("http://", "").replace("https://", "").split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                return True
    except:
        return False

df = pd.read_csv("../outputs/ssl_security_full_analiz.csv", sep=";")
df["SSL Sertifikası Geçerli mi?"] = df["İnternet Adresi"].apply(check_ssl_validity)
df.to_csv("../outputs/ssl_security_full_analiz_ssl_valid.csv", sep=";", index=False, encoding="utf-8-sig")
print("✅ SSL sertifikası sütunu eklendi.")
