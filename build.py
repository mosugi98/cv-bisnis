#!/usr/bin/env python3
"""Bangun halaman statis dari src.html.

  python3 build.py   ->  index.html (Indonesia) dan en/index.html (Inggris)

Edit teks di src.html saja. Teks Indonesia ditulis langsung di elemen,
teks Inggris di atribut data-en (juga data-en-alt dan data-en-aria-label).
Jangan edit index.html atau en/index.html secara manual, file itu ditimpa.
"""
import copy
import json
import os
import urllib.parse
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://mohsuprayogi.com"
OG_IMAGE = SITE + "/og.jpg"
ASSETS = ("foto.jpg", "pelatihan.jpg", "demo.mp4", "demo-poster.jpg")

PAGES = {
    "id": {
        "out": "index.html",
        "url": SITE + "/",
        "prefix": "",
        "href_id": "./",
        "href_en": "en/",
        "title": "dr. Moh. Suprayogi | Dokter Casemix dan Verifikator Klaim JKN",
        "desc": "Dokter umum dan verifikator internal casemix di RSUD Dompu. Membantu rumah sakit meningkatkan klaim INA-CBGs sesuai kaidah: ICD-10, iDRG, VPK/AAK.",
        "locale": "id_ID",
        "alt_locale": "en_US",
        "og_alt": "dr. Moh. Suprayogi, dokter casemix dan verifikator klaim JKN di RSUD Dompu",
        "job": "Dokter Umum dan Verifikator Internal Casemix",
    },
    "en": {
        "out": "en/index.html",
        "url": SITE + "/en/",
        "prefix": "../",
        "href_id": "../",
        "href_en": "./",
        "title": "Dr. Moh. Suprayogi | Casemix Doctor and JKN Claims Verifier",
        "desc": "General practitioner and internal casemix verifier at RSUD Dompu, Indonesia. Helping hospitals raise INA-CBGs claims within the rules: ICD-10, iDRG, VPK/AAK.",
        "locale": "en_US",
        "alt_locale": "id_ID",
        "og_alt": "Dr. Moh. Suprayogi, casemix doctor and JKN claims verifier at RSUD Dompu",
        "job": "General Practitioner and Internal Casemix Verifier",
    },
}

KNOWS = [
    "Casemix", "INA-CBGs", "iDRG", "ICD-10", "ICD-9-CM",
    "Verifikasi Pasca Klaim (VPK)", "Audit Administrasi Klaim (AAK)",
    "Dispute klaim JKN", "Audit potensi fraud klaim",
]

FAVICON_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
    "<rect width='64' height='64' rx='14' fill='#0B1F19'/>"
    "<text x='32' y='45' font-family='Georgia,serif' font-size='40' "
    "text-anchor='middle' fill='#C9A45C'>S</text></svg>"
)


def seo_block(lang):
    p = PAGES[lang]
    other = "en" if lang == "id" else "id"
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "@id": SITE + "/#person",
                "name": "dr. Moh. Suprayogi",
                "alternateName": ["Moh. Suprayogi"],
                "url": SITE + "/",
                "image": SITE + "/foto.jpg",
                "jobTitle": p["job"],
                "email": "mailto:mohsuprayogi17@gmail.com",
                "worksFor": {
                    "@type": "Organization",
                    "name": "RSUD Dompu",
                    "address": {
                        "@type": "PostalAddress",
                        "addressLocality": "Dompu",
                        "addressRegion": "Nusa Tenggara Barat",
                        "addressCountry": "ID",
                    },
                },
                "knowsAbout": KNOWS,
                "knowsLanguage": ["id", "en"],
            },
            {
                "@type": "WebSite",
                "@id": SITE + "/#website",
                "url": SITE + "/",
                "name": "dr. Moh. Suprayogi",
                "inLanguage": ["id", "en"],
                "publisher": {"@id": SITE + "/#person"},
            },
            {
                "@type": "WebPage",
                "@id": p["url"] + "#webpage",
                "url": p["url"],
                "name": p["title"],
                "description": p["desc"],
                "inLanguage": "id" if lang == "id" else "en",
                "isPartOf": {"@id": SITE + "/#website"},
                "about": {"@id": SITE + "/#person"},
                "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
            },
        ],
    }
    esc = lambda s: s.replace("&", "&amp;").replace('"', "&quot;")
    fav = "data:image/svg+xml," + urllib.parse.quote(FAVICON_SVG)
    lines = [
        f"<title>{esc(p['title'])}</title>",
        f'<meta name="description" content="{esc(p["desc"])}">',
        '<meta name="robots" content="index, follow, max-image-preview:large">',
        '<meta name="author" content="dr. Moh. Suprayogi">',
        '<meta name="theme-color" content="#0B1F19">',
        f'<link rel="canonical" href="{p["url"]}">',
        f'<link rel="alternate" hreflang="id" href="{PAGES["id"]["url"]}">',
        f'<link rel="alternate" hreflang="en" href="{PAGES["en"]["url"]}">',
        f'<link rel="alternate" hreflang="x-default" href="{PAGES["id"]["url"]}">',
        f'<link rel="icon" href="{fav}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="dr. Moh. Suprayogi">',
        f'<meta property="og:title" content="{esc(p["title"])}">',
        f'<meta property="og:description" content="{esc(p["desc"])}">',
        f'<meta property="og:url" content="{p["url"]}">',
        f'<meta property="og:locale" content="{p["locale"]}">',
        f'<meta property="og:locale:alternate" content="{p["alt_locale"]}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{esc(p["og_alt"])}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(p["title"])}">',
        f'<meta name="twitter:description" content="{esc(p["desc"])}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
        '<script type="application/ld+json">'
        + json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
        + "</script>",
    ]
    return "\n".join(lines)


def set_html(el, html):
    frag = BeautifulSoup(html, "html.parser")
    el.clear()
    for c in list(frag.contents):
        el.append(c.extract())


def build(lang, src):
    p = PAGES[lang]
    soup = BeautifulSoup(src, "html.parser")
    soup.html["lang"] = lang

    for el in soup.find_all(True):
        if lang == "en":
            if el.has_attr("data-en"):
                set_html(el, el["data-en"])
            if el.has_attr("data-en-alt"):
                el["alt"] = el["data-en-alt"]
            if el.has_attr("data-en-aria-label"):
                el["aria-label"] = el["data-en-aria-label"]
        for a in ("data-en", "data-en-alt", "data-en-aria-label"):
            if el.has_attr(a):
                del el[a]

    for a in soup.select(".lang a[data-lang]"):
        l = a["data-lang"]
        a["href"] = p["href_" + l]
        if l == lang:
            a["aria-current"] = "true"
        del a["data-lang"]

    if p["prefix"]:
        for el in soup.find_all(src=True):
            if el["src"] in ASSETS:
                el["src"] = p["prefix"] + el["src"]
        for el in soup.find_all(poster=True):
            if el["poster"] in ASSETS:
                el["poster"] = p["prefix"] + el["poster"]

    html = str(soup)
    assert "<!--SEO-->" in html
    html = html.replace("<!--SEO-->", seo_block(lang))
    return html


def main():
    src = open(os.path.join(ROOT, "src.html"), encoding="utf-8").read()
    for lang, p in PAGES.items():
        out = os.path.join(ROOT, p["out"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(build(lang, src))
        print("ok", p["out"])


if __name__ == "__main__":
    main()
