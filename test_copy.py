import time
import pyautogui
import pyperclip

print("You have 5 seconds...")
time.sleep(5)

pyautogui.hotkey("ctrl", "c")
time.sleep(1)

print("Clipboard:")
print(repr(pyperclip.paste()))