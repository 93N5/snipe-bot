import random
import time
import pyautogui
import pygetwindow as gw
import pytesseract
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_random_time():
    return random.randint(1, 3)

def main():
    fcul = "FC Ultimate Team Web App"
    browser = gw.getWindowsWithTitle(fcul)[0]

    # player_name = os.getenv("PLAYER_NAME")
    # gold_rare= os.getenv("GOLD_RARE")
    # fantasy_hero = os.getenv("FANTASY_HERO")
    # set_program_loop = int(os.getenv("SET_PROGRAM_LOOP"))
    # set_trading_loop = int(os.getenv("SET_TRADING_LOOP"))
    # set_timeout = int(os.getenv("SET_TIMEOUT"))
    # max_buy_now_price = os.getenv("MAX_BUY_NOW_PRICE")

    player_name = "voller"
    gold_rare= "no"
    fantasy_hero = "yes"
    set_program_loop = 100
    set_trading_loop = 10000
    set_timeout = 100
    max_buy_now_price = "150000"

    print("player name:", player_name)
    print("gold rare:", gold_rare)
    print("set program loop:", set_program_loop)
    print("set trading loop:", set_trading_loop)
    print("set timeout:", set_timeout)
    print("max buy now price:", max_buy_now_price)

    if fcul in browser.title:
        browser.activate()
        if not browser.isMaximized:
            browser.maximize()

        counter = 0

        while True:
            if counter == set_program_loop:
                break

            print(f"snipe started: {datetime.now()}")

            time.sleep(get_random_time())

            transfer_market_button_x = 650
            transfer_market_button_y = 400

            pyautogui.click(transfer_market_button_x, transfer_market_button_y)

            time.sleep(get_random_time())

            type_player_button_x = 950
            type_player_button_y = 420

            pyautogui.click(type_player_button_x, type_player_button_y)
            pyautogui.typewrite(player_name)

            time.sleep(get_random_time())

            player_search_button_x = 970
            player_search_button_y = 490

            pyautogui.click(player_search_button_x, player_search_button_y)

            if gold_rare == "yes":
                time.sleep(get_random_time())

                select_quality_button_x = 880
                select_quality_button_y = 460

                pyautogui.click(select_quality_button_x, select_quality_button_y)

                time.sleep(get_random_time())

                select_gold_button_x = 880
                select_gold_button_y = 600

                pyautogui.click(select_gold_button_x, select_gold_button_y)

                time.sleep(get_random_time())

                rarity_button_x = 1080
                rarity_button_y = 450

                pyautogui.click(rarity_button_x, rarity_button_y)

                time.sleep(get_random_time())

                select_rare_rarity_button_x = 1080
                select_rare_rarity_button_y = 550

                pyautogui.click(select_rare_rarity_button_x, select_rare_rarity_button_y)

            if fantasy_hero == "yes":
                time.sleep(get_random_time())

                select_quality_button_x = 950
                select_quality_button_y = 460

                center_x, center_y = (1920 // 2, 1080 // 2)
                req_x, req_y = (center_x, center_y)

                check_quality = pyautogui.screenshot(region=(req_x - 430, req_y - 200, 200, 300))
                check_quality.save("assets/check_quality.png")

                ocr_result3 = pytesseract.image_to_string("assets/check_quality.png", config = "--psm 6")

                if "Special" in ocr_result3:
                    pyautogui.click(select_quality_button_x, select_quality_button_y)

                pyautogui.click(select_quality_button_x, select_quality_button_y)

                time.sleep(get_random_time())

                select_fantasy_hero_button_x = 880
                select_fantasy_hero_button_y = 680

                pyautogui.click(select_fantasy_hero_button_x, select_fantasy_hero_button_y)

                time.sleep(get_random_time())

                rarity_button_x = 1080
                rarity_button_y = 460

                pyautogui.click(rarity_button_x, rarity_button_y)

                # click for scroll
                pyautogui.click(1500, 600)

                time.sleep(get_random_time())

                select_rare_rarity_button_x = 1080
                select_rare_rarity_button_y = 700

                pyautogui.click(select_rare_rarity_button_x, select_rare_rarity_button_y)

            time.sleep(get_random_time())

            minus_button_x = 500
            minus_button_y = 790

            plus_button_x = 950
            plus_button_y = 790

            go_back_button_x = 140
            go_back_button_y = 210

            min_bid_price_button_x = 580
            min_bid_price_button_y = 790

            pyautogui.click(min_bid_price_button_x, min_bid_price_button_y)
            pyautogui.typewrite("150")

            time.sleep(get_random_time())

            max_buy_now_price_button_x = 1140
            max_buy_now_price_button_y = 895

            pyautogui.click(max_buy_now_price_button_x, max_buy_now_price_button_y)
            pyautogui.typewrite(max_buy_now_price)

            time.sleep(get_random_time())

            search_button_x = 1140
            search_button_y = 920
            pyautogui.click(search_button_x, search_button_y)

            snipe_counter = 1

            # snipe loop function
            while True:
                if snipe_counter == set_trading_loop:
                    break

                time.sleep(0.3)

                center_x, center_y = (1920 // 2, 1080 // 2)
                results__x, results__y = (center_x, center_y + 100)

                check_search = pyautogui.screenshot(region=(results__x - 80, results__y - 10, 250, 100))
                check_search.save("assets/check_search.png")

                ocr_result1 = pytesseract.image_to_string("assets/check_search.png", config = "--psm 6")

                if not "No results" in ocr_result1:
                    buy_item_button_x = 1400
                    buy_item_button_y = 750
                    pyautogui.click(buy_item_button_x, buy_item_button_y)

                    get_item_button_x = 970
                    get_item_button_y = 620
                    pyautogui.click(get_item_button_x, get_item_button_y)

                    now = datetime.now()
                    now_string = now.strftime("%d_%m_%Y_%H_%M_%S")

                    if not os.path.exists(f"assets/{player_name}"):
                        os.makedirs(f"assets/{player_name}")

                    time.sleep(2)

                    check_player = pyautogui.screenshot()

                    player_image = f"{player_name}/{now_string}.png"
                    check_player.save(f"assets/{player_image}")

                    print(f"player found at: {now}; and tried to buy the player:", player_name)
                
                time.sleep(get_random_time())

                pyautogui.click(go_back_button_x, go_back_button_y)

                time.sleep(1)

                center_x, center_y = (1920 // 2, 1080 // 2)
                rec_x, rec_y = (center_x, center_y + 400)

                check_bid_price = pyautogui.screenshot(region=(rec_x - 430, rec_y - 200, 200, 300))
                check_bid_price.save("assets/check_bid_price.png")

                ocr_result2 = pytesseract.image_to_string("assets/check_bid_price.png", config = "--psm 6")

                if "150" in ocr_result2:
                    pyautogui.click(minus_button_x, minus_button_y)
                else:
                    pyautogui.click(plus_button_x, plus_button_y)

                time.sleep(1)

                pyautogui.click(search_button_x, search_button_y)

                snipe_counter += 1

            time.sleep(get_random_time())

            pyautogui.click(go_back_button_x, go_back_button_y)

            time.sleep(1)

            pyautogui.click(go_back_button_x, go_back_button_y)

            counter += 1

            time.sleep(set_timeout)

        print(f"snipe ended: {datetime.now()}")

        browser.minimize()

if __name__ == '__main__':
    main()

