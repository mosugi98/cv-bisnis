# cv-bisnis

Website CV dan portofolio dr. Moh. Suprayogi (dokter umum dan verifikator internal casemix, RSUD Dompu). Satu halaman, dwibahasa: `/` (Indonesia) dan `/en/` (Inggris), masing-masing halaman statis agar bisa diindeks Google.

## Isi

| File | Fungsi |
|---|---|
| `src.html` | **Sumber utama.** Edit teks dan tampilan di sini |
| `build.py` | Membuat `index.html` (ID) dan `en/index.html` (EN) dari `src.html` |
| `index.html`, `en/index.html` | Hasil build. Jangan diedit manual, akan tertimpa |
| `og.jpg` | Gambar pratinjau saat tautan dibagikan (1200x630) |
| `sitemap.xml`, `robots.txt` | Untuk mesin pencari |
| `foto.jpg` | Foto profil di bagian atas |
| `pelatihan.jpg` | Foto bagian Pelatihan |
| `demo.mp4`, `demo-poster.jpg` | Video demo Skrining Rawat Inap Harian dan gambar sampulnya |

## Menayangkan dengan GitHub Pages

1. Buka **Settings > Pages**.
2. Pada **Build and deployment**, pilih **Deploy from a branch**, cabang `main`, folder `/ (root)`, lalu Save.
3. Situs tayang di `https://mosugi98.github.io/cv-bisnis/` dalam beberapa menit.

## Memakai domain sendiri

Domain situs ini: `mohsuprayogi.com` (tercatat di file `CNAME`).

1. Di **Settings > Pages > Custom domain**, isi domain Anda lalu Save. GitHub membuat file `CNAME` otomatis.
2. Di panel DNS registrar, tambahkan empat A record untuk domain utama:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Tambahkan CNAME `www` ke `mosugi98.github.io`.
4. Setelah DNS aktif, centang **Enforce HTTPS** di halaman Pages.

## Catatan

- Video demo memakai data contoh. Jangan mengganti dengan rekaman yang memuat data pasien sungguhan.
- Ubah isi halaman di `src.html`. Teks Indonesia ada di isi elemen, teks Inggris di atribut `data-en` (juga `data-en-alt`, `data-en-aria-label`).
- Setelah mengedit, jalankan `python3 build.py` (butuh `pip install beautifulsoup4`), lalu commit `src.html`, `index.html`, dan `en/index.html` bersama.
- Judul, deskripsi, dan data JSON-LD untuk SEO ada di bagian atas `build.py`.
- Setelah situs tayang, daftarkan `https://mohsuprayogi.com/sitemap.xml` di Google Search Console.
