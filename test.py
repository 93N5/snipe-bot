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

        center_x, center_y = (1920 // 2, 1080 // 2)
        results__x, results__y = (center_x, center_y + 100)

        check_search = pyautogui.screenshot(region=(results__x - 80, results__y - 10, 250, 100))
        check_search.save("assets/check_search.png")

        ocr_result1 = pytesseract.image_to_string("assets/check_search.png", config = "--psm 6")

        if not "No results" in ocr_result1:
            print("player found")
        else:
            print("player not found")

        time.sleep(1)

        browser.minimize()

if __name__ == "__main__":
    main()