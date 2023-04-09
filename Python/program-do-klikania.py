import pyautogui
import time
import keyboard

def clicker(interval):
    paused = False
    while True:
        if keyboard.is_pressed('f10'):  # Sprawdzenie, czy przycisk F10 został wciśnięty
            print("Zatrzymano skrypt.")
            break

        if keyboard.is_pressed('f9'):  # Sprawdzenie, czy przycisk F9 został wciśnięty
            if not paused:
                print("Wstrzymano skrypt.")
            else:
                print("Wznowiono skrypt.")
            paused = not paused
            time.sleep(0.5)  # Dodaj opóźnienie, aby uniknąć wielokrotnego przełączania

        if not paused:
            pyautogui.click()
            time.sleep(interval)

if __name__ == "__main__":
    interval = 0.01  # Kliknięcie co 0.01 sekundy (100 razy na sekundę)
    clicker(interval)
