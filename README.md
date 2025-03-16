# Bot Auto Klik TikTok Live

## Deskripsi

Skrip ini digunakan untuk mendapatkan koordinat posisi mouse dan melakukan klik otomatis di TikTok Live.

## Persyaratan

Sebelum menjalankan skrip, pastikan Anda telah menginstal Python dan modul yang diperlukan.

### Instalasi Modul

Jalankan perintah berikut di terminal:

```bash
pip install pyautogui
```

## 1. Menjalankan `get_position.py`

Skrip ini digunakan untuk mendapatkan koordinat posisi mouse.

### Cara Penggunaan:

1. Jalankan skrip dengan perintah:
   ```bash
   python get_position.py
   ```
2. Arahkan kursor ke posisi yang ingin diklik.
3. Tekan `Enter`, dan koordinat akan ditampilkan di terminal.
4. Catat koordinat tersebut untuk digunakan dalam `auto_klik.py`.

## 2. Menjalankan `auto_klik.py`

Skrip ini digunakan untuk melakukan klik otomatis pada posisi yang telah ditentukan.

### Cara Penggunaan:

1. Edit `auto_klik.py` dan masukkan koordinat yang didapat dari `get_position.py`.
2. Jalankan skrip dengan perintah:
   ```bash
   python auto_klik.py
   ```
3. Skrip akan mulai melakukan klik otomatis.
4. Tekan `Enter` di terminal untuk menghentikan bot.

## Catatan

- Pastikan TikTok Live sudah terbuka sebelum menjalankan `auto_klik.py`.
- Jangan gunakan bot ini untuk tujuan yang melanggar kebijakan platform.
- Jika ingin menyesuaikan kecepatan klik, ubah nilai `time.sleep()` dalam `auto_klik.py`.
