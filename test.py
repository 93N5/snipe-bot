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

        select_quality_button_x = 950
        select_quality_button_y = 460

        center_x, center_y = (1920 // 2, 1080 // 2)
        req_x, req_y = (center_x, center_y)

        check_quality = pyautogui.screenshot(region=(req_x - 430, req_y - 200, 200, 300))
        check_quality.save("assets/check_quality.png")

        ocr_result3 = pytesseract.image_to_string("assets/check_quality.png", config = "--psm 6")

        print(ocr_result3)

        if "Special" in ocr_result3:
            pyautogui.click(select_quality_button_x, select_quality_button_y)

        # button_x = 950
        # button_y = 460
        # pyautogui.moveTo(button_x, button_y)

        time.sleep(1)

        browser.minimize()

if __name__ == "__main__":
    main()