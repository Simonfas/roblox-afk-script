import pyautogui
import pygetwindow as gw
import time
import psutil
import win32process
import win32gui
from pynput.keyboard import Controller

keyboard = Controller()

TARGET_WINDOW = "Roblox"

def get_active_window_title_and_process():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        title = win32gui.GetWindowText(hwnd)
        return title, process.name()
    except Exception:
        return None, None

def is_target_window_active():
    active_window = gw.getActiveWindow()
    if active_window and TARGET_WINDOW.lower() in active_window.title.lower():
        return True
    return False

print(f"Venter på at {TARGET_WINDOW} bliver aktivt vindue... (tryk Ctrl+C i terminalen for at stoppe)")

last_title = None

try:
    while True:
        title, process = get_active_window_title_and_process()
        if title != last_title and title:
            print(f"Aktivt vindue: '{title}'  |  Proces: {process}")
            last_title = title

        if is_target_window_active():
            print("Holder A nede i 5 sekunder")
            keyboard.press('a')
            time.sleep(5)
            keyboard.release('a')

            time.sleep(0.2)

            print("Holder D nede i 5 sekunder")
            keyboard.press('d')
            time.sleep(5)
            keyboard.release('d')

            time.sleep(0.2)
        else:
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Afsluttet.")
