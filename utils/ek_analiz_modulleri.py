import pandas as pd
from bs4 import BeautifulSoup

def safe_eval(val, default):
    try:
        return eval(val) if isinstance(val, str) else val
    except:
        return default

def analyze_additional_features(df: pd.DataFrame) -> pd.DataFrame:
    # Gerekli sütunlar yoksa boş geç
    if 'headers' not in df.columns:
        df['headers'] = [{} for _ in range(len(df))]
    else:
        df['headers'] = df['headers'].apply(lambda x: safe_eval(x, {}))

    if 'html' not in df.columns:
        df['html'] = ['' for _ in range(len(df))]

    if 'response_bytes' not in df.columns:
        df['response_bytes'] = [b'' for _ in range(len(df))]
    else:
        df['response_bytes'] = df['response_bytes'].apply(lambda x: str(x).encode('utf-8'))

    if 'http_methods' not in df.columns:
        df['http_methods'] = [[] for _ in range(len(df))]
    else:
        df['http_methods'] = df['http_methods'].apply(lambda x: safe_eval(x, []))

    def extract_features(row):
        headers = row['headers']
        html = row['html']
        response_bytes = row['response_bytes']
        methods = row['http_methods']

        hsts = headers.get('strict-transport-security', '').lower()
        cors = headers.get('access-control-allow-origin')

        return pd.Series({
            'CSP_Header': 'content-security-policy' in headers,
            'X_Frame_Options': 'x-frame-options' in headers,
            'X_Content_Type_Options': 'x-content-type-options' in headers,
            'HSTS_Preload': 'preload' in hsts,
            'HSTS_Include_Subdomains': 'includesubdomains' in hsts,
            'HSTS_Max_Age': 'max-age' in hsts,
            'CORS_Wildcard': cors == '*',
            'Dangerous_HTTP_Methods': 'OPTIONS' in methods or 'TRACE' in methods,
            'Canonical_Tag': '<link rel="canonical"' in html,
            'Meta_Description': '<meta name="description"' in html.lower(),
            'OpenGraph_Tags': 'property="og:' in html.lower(),
            'Lazy_Loading': 'loading="lazy"' in html.lower(),
            'Favicon': '<link rel="icon"' in html.lower(),
            'Google_Fonts': 'fonts.googleapis.com' in html,
            'Page_Size_KB': round(len(response_bytes) / 1024, 2),
            'DOM_Element_Count': len(BeautifulSoup(html, 'html.parser').find_all()),
            'Google_Analytics': 'googletagmanager.com' in html or 'google-analytics.com' in html,
            'Meta_Viewport': '<meta name="viewport"' in html.lower(),
            'Structured_Data': 'application/ld+json' in html,
        })

    ek_sutunlar = df.apply(extract_features, axis=1)
    return pd.concat([df, ek_sutunlar], axis=1)
