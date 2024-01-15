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
        rec_x, rec_y = (center_x, center_y + 400)

        check_bid_price = pyautogui.screenshot(region=(rec_x - 430, rec_y - 200, 200, 300))
        check_bid_price.save("assets/check_bid_price.png")

        ocr_result2 = pytesseract.image_to_string("assets/check_bid_price.png", config = "--psm 6")

        print(ocr_result2)

        browser.minimize()

if __name__ == "__main__":
    main()