import random
import time
import os
from dotenv import load_dotenv
import pygetwindow as gw
import pyautogui

load_dotenv()

def get_random_time():
    return random.randint(1, 3)

def main():
    fcul = "FC Ultimate Team Web App"
    browser = gw.getWindowsWithTitle(fcul)[0]

    player = os.getenv("PLAYER_NAME")
    loop = int(os.getenv("SET_LOOP"))
    timeout = int(os.getenv("SET_TIMEOUT"))

    if fcul in browser.title:
        print("Found tab with title: ", browser.title)
        browser.activate()
        
        if not browser.isMaximized:
            browser.maximize()
        
        counter = 0

        print(player, loop, timeout)

        while True:
            if counter == loop:
                break
            
            time.sleep(get_random_time())

            pyautogui.moveTo

            counter += 1


if __name__ == '__main__':
    main()
