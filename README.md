# Auto Click Bot

Script ini adalah bot auto-clicker sederhana yang digunakan untuk melakukan klik otomatis pada posisi tertentu di layar. Script ini dibuat untuk tujuan **edukasi dan eksperimen** dalam memahami otomatisasi.

## 🚀 Fitur

- Klik otomatis di posisi yang ditentukan
- Berjalan hingga pengguna menekan **ENTER** untuk berhenti

## 📌 Persyaratan

Pastikan Python sudah terinstal di sistem Anda.

- Python 3.x
- `pyautogui`
- `threading` (bawaan Python)

## 🔧 Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. **Buat virtual environment** (opsional, tapi disarankan)
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # Linux/macOS
   myenv\Scripts\activate     # Windows
   ```
3. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Cara Menjalankan

### **1. Dapatkan Koordinat Klik**

Jalankan script `get_position.py` untuk mengetahui posisi kursor:

```bash
python get_position.py
```

Arahkan kursor ke posisi yang diinginkan, lalu tekan **ENTER** untuk mendapatkan koordinatnya.

### **2. Jalankan Auto Clicker**

```bash
python auto_klik.py
```

Setelah dijalankan, **buka browser** dan arahkan ke halaman yang ingin diklik.

Tekan **ENTER** untuk menghentikan bot.

## ⚠ Disclaimer

Script ini dibuat hanya untuk **tujuan edukasi** dan **eksperimen pribadi**. Penggunaan script ini **sepenuhnya tanggung jawab pengguna**.

Kami **tidak bertanggung jawab** atas penggunaan yang melanggar kebijakan platform tertentu.

## 📜 Lisensi

Lisensi MIT - Bebas digunakan, tetapi tanggung jawab sepenuhnya ada pada pengguna.

---
