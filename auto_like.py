import pyautogui
import time
import threading

# Koordinat klik (ubah sesuai kebutuhan)
base_x, base_y = 1246, 667 

# Variabel global untuk menghentikan loop
running = True

def stop_bot():
    """Fungsi untuk menghentikan bot dengan menekan ENTER di terminal."""
    global running
    input("Tekan ENTER untuk berhenti...\n")
    running = False

# Fungsi `stop_bot()` berjalan di thread lain agar tidak mengganggu loop utama
threading.Thread(target=stop_bot, daemon=True).start()

print("Buka browser dan arahkan ke TikTok Live dalam 5 detik...")
time.sleep(5)

print("Bot mulai...")

while running:
    # Klik pada koordinat yang telah ditentukan
    pyautogui.click(base_x, base_y)

    # Jeda antarklik
    time.sleep(0.125)

print("Bot dihentikan.")
