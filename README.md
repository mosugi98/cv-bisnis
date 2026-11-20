# cv-bisnis

Website CV dan portofolio dr. Moh. Suprayogi (dokter umum dan verifikator internal casemix, RSUD Dompu). Satu halaman, dwibahasa (ID/EN), tanpa build step.

## Isi

| File | Fungsi |
|---|---|
| `index.html` | Seluruh halaman (HTML, CSS, JavaScript) |
| `foto.jpg` | Foto profil di bagian atas |
| `pelatihan.jpg` | Foto bagian Pelatihan |
| `demo.mp4`, `demo-poster.jpg` | Video demo Skrining Rawat Inap Harian dan gambar sampulnya |

## Menayangkan dengan GitHub Pages

1. Buka **Settings > Pages**.
2. Pada **Build and deployment**, pilih **Deploy from a branch**, cabang `main`, folder `/ (root)`, lalu Save.
3. Situs tayang di `https://mosugi98.github.io/cv-bisnis/` dalam beberapa menit.

## Memakai domain sendiri

1. Di **Settings > Pages > Custom domain**, isi domain Anda lalu Save. GitHub membuat file `CNAME` otomatis.
2. Di panel DNS registrar, tambahkan empat A record untuk domain utama:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Tambahkan CNAME `www` ke `mosugi98.github.io`.
4. Setelah DNS aktif, centang **Enforce HTTPS** di halaman Pages.

## Catatan

- Video demo memakai data contoh. Jangan mengganti dengan rekaman yang memuat data pasien sungguhan.
- Ubah isi halaman langsung di `index.html`. Teks Indonesia ada di isi elemen, teks Inggris di atribut `data-en`.
