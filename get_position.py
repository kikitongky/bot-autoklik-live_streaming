import pyautogui
import time

print("Arahkan kursor ke area yang ingin diklik dalam 5 detik...")
time.sleep(5)  # Tunggu 5 detik
print("Koordinat mouse:", pyautogui.position())  # Cetak posisi mouse
