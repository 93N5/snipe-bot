import random
import time
import pyautogui
import pygetwindow as gw
import pytesseract
from dotenv import load_dotenv
import os

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    fcul = "FC Ultimate Team Web App"
    browser = gw.getWindowsWithTitle(fcul)[0]

    if fcul in browser.title:
        browser.activate()
        if not browser.isMaximized:
            browser.maximize()

        time.sleep(1)

        get_item_button_x = 970
        get_item_button_y = 600
        pyautogui.moveTo(get_item_button_x, get_item_button_y)

        time.sleep(1)

        # browser.minimize()

if __name__ == "__main__":
    main()