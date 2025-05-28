import ssl
import socket
import requests
from datetime import datetime

def kontrol_ssl(domain):
    result = {"https_var": False, "ssl_gecerli": False, "not_before": None, "not_after": None}
    try:
        domain = domain.replace("http://", "").replace("https://", "").split("/")[0]
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
        conn.settimeout(5)
        conn.connect((domain, 443))
        result["https_var"] = True
        cert = conn.getpeercert()
        result["not_before"] = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')
        result["not_after"] = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        now = datetime.utcnow()
        result["ssl_gecerli"] = result["not_before"] <= now <= result["not_after"]
    except:
        pass
    finally:
        try:
            conn.close()
        except:
            pass
    return result

def kontrol_security_headers(domain):
    headers_result = {
        "Strict-Transport-Security": False,
        "Content-Security-Policy": False,
        "X-Frame-Options": False,
        "X-Content-Type-Options": False,
        "Referrer-Policy": False
    }
    try:
        domain = domain.replace("http://", "").replace("https://", "").split("/")[0]
        url = "https://" + domain
        response = requests.get(url, timeout=5, allow_redirects=True)
        for key in headers_result:
            if key in response.headers:
                headers_result[key] = True
    except:
        pass
    return headers_result

def hesapla_owasp_ve_skor(ssl_info, headers):
    risks = {
        "A02 - Cryptographic Failure": not ssl_info["ssl_gecerli"],
        "A05 - Security Misconfiguration": not headers["X-Frame-Options"] or not headers["X-Content-Type-Options"],
        "A08 - Software/Data Integrity Failure": not headers["Strict-Transport-Security"] or not headers["Content-Security-Policy"]
    }
    skor = sum(headers.values())
    return risks, skor
