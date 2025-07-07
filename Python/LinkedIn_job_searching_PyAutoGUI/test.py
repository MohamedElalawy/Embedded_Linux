import pyautogui
while True:
        x, y = pyautogui.position()
        print(f"Current Mouse Position: X={x}, Y={y}", end='\r')