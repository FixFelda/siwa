# 🧪 Penetapan Kadar Fosfat – Spektrofotometer Digital

Kalkulator dan simulasi 3D spektrofotometer UV-Vis untuk penetapan kadar fosfat
dengan metode asam askorbat.

- `index.html` – aplikasi utama (HTML + JavaScript + three.js, berdiri sendiri)
- `app.py` – pembungkus Streamlit
- `.github/workflows/pages.yml` – deploy otomatis ke GitHub Pages

## Jalankan lokal

**Versi Streamlit**

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Versi HTML biasa** – cukup buka `index.html` di browser.

## Upload ke GitHub

```bash
git init
git add .
git commit -m "First commit: kalkulator fosfat"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```

## Deploy

### Opsi A – GitHub Pages (paling mudah, gratis)
1. Di repo GitHub: **Settings → Pages → Source: GitHub Actions**.
2. Push ke branch `main`. Situs akan aktif di
   `https://USERNAME.github.io/NAMA-REPO/`.

### Opsi B – Streamlit Community Cloud
1. Buka <https://share.streamlit.io> dan login dengan GitHub.
2. **Create app** → pilih repo ini, branch `main`, main file `app.py`.
3. Klik **Deploy**.

## Catatan
Aplikasi memuat three.js (cdnjs) dan font IBM Plex Sans (Google Fonts), jadi
butuh koneksi internet saat dibuka.
