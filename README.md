# 🎬 Video to Teks — Transkripsi Otomatis dengan Whisper

Notebook Colab ini dirancang untuk membantu proses lengkap dalam mengunduh video, mengekstrak audio, dan mentranskripsikannya menjadi teks menggunakan model **Whisper dari OpenAI**.

---

## 🚀 Fitur Utama

### 🧩 Download Video
- ✅ Google Drive
- ✅ Direct Download (MP4, MKV, dll)
- ✅ Link streaming (.m3u8)
- ✅ Bisa pilih manual atau deteksi otomatis

### 🎧 Ekstraksi Audio
- Ekstraksi audio lossless (WAV 16kHz mono)
- Penamaan otomatis sesuai nama video
- Overwrite otomatis jika file sudah ada

### 🧠 Transkripsi Otomatis (Whisper)
- Dukungan model: `tiny`, `base`, `small`, `medium`, `large`
- Transkripsi multi-segmen + timestamp
- Simpan ke `.json`

### 📄 Output Lanjutan
- ✅ Ringkasan hasil transkrip
- ✅ Ekspor ke subtitle `.srt` (auto wrap teks)
- ✅ Embed subtitle `.srt` ke video (.mkv softsub)
- ✅ Kompres output ke `.zip`
- ✅ Hapus otomatis file sementara

### 🧪 Alat Tambahan
- Deteksi apakah file audio **lossless atau lossy**
- Input manual path untuk semua langkah (fleksibel)

---

## 📁 Struktur Folder
```
/transkrip_project/
├── video/        ← hasil video download
├── audio/        ← hasil ekstrak audio
├── output/       ← hasil transkrip, subtitle, video akhir
├── logs/         ← log download yt-dlp
```

---

## 📚 Library yang Digunakan
- `whisper`
- `yt-dlp`
- `ffmpeg`, `ffmpeg-python`
- `gdown`, `tqdm`
- `m3u8downloader`

Semua library akan otomatis diinstal saat notebook dijalankan.

---

## ▶️ Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lIlSkaSkaSkalIl/Video-to-Teks/blob/e2a3562961f8fd8ba0d444faab80b0a13c897106/Video%20to%20Teks.ipynb)

---

## 📦 Kompres Otomatis
Output transkrip dan subtitle bisa langsung dikompres ke ZIP agar mudah diunduh sekaligus.

---

## 🛡️ Privasi & Keamanan
Notebook ini **tidak menyimpan cookies, token, atau data pribadi**. Semua file hanya tersimpan selama runtime aktif.

---

## 👨‍💻 Author

Proyek ini dikembangkan oleh [lIlSkaSkaSkalIl](https://github.com/lIlSkaSkaSkalIl),  
dengan tujuan menyediakan solusi praktis untuk transkripsi video otomatis berbasis Whisper dan Python.  
Terbuka untuk kolaborasi dan pengembangan lebih lanjut melalui kontribusi komunitas.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License.
