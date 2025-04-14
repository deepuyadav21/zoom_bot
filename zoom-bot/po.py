import pyautogui
import time

print("You have 5 seconds to move your mouse to the desired position...")

time.sleep(5)
print("Mouse position:", pyautogui.position())
a,b=pyautogui.position()
pyautogui.moveTo(a, b+20, duration=1)
