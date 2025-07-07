import pyautogui
import subprocess
import time
from PIL import Image
import win32clipboard
import io

def open_chrome():
    print("Opening Chrome with Default profile...")
    subprocess.Popen([
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        '--profile-directory=Default'
    ])
    time.sleep(5)

def open_linkedin_jobs():
    print("Opening LinkedIn Jobs page...")
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write('https://www.linkedin.com/jobs', interval=0.07)
    pyautogui.press('enter')
    time.sleep(7)

def find_and_click(image_path, confidence=0.8):
    print(f"Looking for {image_path}...")
    location = None
    while location is None:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        time.sleep(1)
    print(f"Found {image_path} at {location}")
    pyautogui.click(location)

def search_job(job_title):
    find_and_click('LinkedInSearchBox.png')
    time.sleep(1)
    pyautogui.write(job_title, interval=0.05)
    pyautogui.press('enter')
    time.sleep(5)

def take_screenshots_with_scroll():
    screenshot1 = pyautogui.screenshot()
    screenshot1.save('linkedin_search_result_1.png')
    print("First screenshot saved as linkedin_search_result_1.png")

    pyautogui.moveTo(450, 450, duration=0.5)
    pyautogui.scroll(-800)
    print("Scrolled down.")
    time.sleep(2)

    screenshot2 = pyautogui.screenshot()
    screenshot2.save('linkedin_search_result_2.png')
    print("Second screenshot saved as linkedin_search_result_2.png")

def open_whatsapp():
    print("Opening WhatsApp Web...")
    pyautogui.hotkey('ctrl', 't')  # Open new tab
    time.sleep(1)
    pyautogui.write('https://web.whatsapp.com', interval=0.1)
    pyautogui.press('enter')
    time.sleep(15)


def send_image_to_clipboard(image_path):
    image = Image.open(image_path)

    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # BMP header fix
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def send_screenshots_to_number():
    print("Finding WhatsApp search box...")
    find_and_click('WhatsAppSearchBox.png')
    time.sleep(1)
    pyautogui.write('01070271829', interval=0.05)
    pyautogui.press('enter')
    time.sleep(2)

    print("Copying first screenshot to clipboard...")
    send_image_to_clipboard('linkedin_search_result_1.png')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    print("Copying second screenshot to clipboard...")
    send_image_to_clipboard('linkedin_search_result_2.png')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.press('enter')
    print("Screenshots sent!")

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    open_chrome()
    open_linkedin_jobs()
    search_job('ُEmbedded Software Engineer')
    take_screenshots_with_scroll()
    open_whatsapp()
    time.sleep(3)
    send_screenshots_to_number()

