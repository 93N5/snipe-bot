import random
import time
import pyautogui
import pygetwindow as gw
import pytesseract
import os


def get_random_time():
    return random.randint(1, 3)

def start():
    fcul = "FC Ultimate Team Web App"
    browser = gw.getWindowsWithTitle(fcul)[0]

    player_name = os.getenv("PLAYER_NAME")
    set_program_loop = int(os.getenv("SET_PROGRAM_LOOP"))
    set_trading_loop = int(os.getenv("SET_TRADING_LOOP"))
    set_timeout = int(os.getenv("SET_TIMEOUT"))
    max_buy_now_price = os.getenv("MAX_BUY_NOW_PRICE")
    list_player_price = os.getenv("LIST_PLAYER_PRICE")

    if fcul in browser.title:
        browser.activate()
        if not browser.isMaximized:
            browser.maximize()

        counter = 0

        while True:
            if counter == set_program_loop:
                break

            time.sleep(get_random_time())

            transfer_market_button_x = 650
            transfer_market_button_y = 400
            pyautogui.click(transfer_market_button_x, transfer_market_button_y)

            time.sleep(get_random_time())

            type_player_button_x = 970
            type_player_button_y = 350
            pyautogui.click(type_player_button_x, type_player_button_y)
            pyautogui.typewrite(player_name)

            time.sleep(get_random_time())

            player_search_button_x = 970
            player_search_button_y = 430
            pyautogui.click(player_search_button_x, player_search_button_y)

            time.sleep(get_random_time())

            minus_button_x = 550
            minus_button_y = 700

            plus_button_x = 970
            plus_button_y = 700

            go_back_button_x = 140
            go_back_button_y = 180

            min_bid_price_button_x = 580
            min_bid_price_button_y = 700
            pyautogui.click(min_bid_price_button_x, min_bid_price_button_y)
            pyautogui.typewrite("150")

            time.sleep(get_random_time())

            max_buy_now_price_button_x = 1140
            max_buy_now_price_button_y = 840
            pyautogui.click(max_buy_now_price_button_x, max_buy_now_price_button_y)
            pyautogui.typewrite(max_buy_now_price)

            time.sleep(get_random_time())

            search_button_x = 1140
            search_button_y = 920
            pyautogui.click(search_button_x, search_button_y)

            snipe_counter = 1

            time.sleep(1)

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
                    buy_item_button_y = 680
                    pyautogui.click(buy_item_button_x, buy_item_button_y)

                    get_item_button_x = 970
                    get_item_button_y = 580
                    pyautogui.click(get_item_button_x, get_item_button_y)

                    time.sleep(1)

                    center_x, center_y = (1920 // 2, 1080 // 2)
                    right_x, right_y = (center_x + 300, center_y - 100)

                    check_item = pyautogui.screenshot(region=(right_x, right_y, 300, 100))
                    check_item.save("assets/check_item.png")

                    ocr_result3 = pytesseract.image_to_string("assets/check_item.png", config = "--psm 6")

                    if "Congratulations" in ocr_result3:
                        time.sleep(get_random_time())

                        list_on_transfermarket_button_x = 1260
                        list_on_transfermarket_button_y = 570
                        pyautogui.click(list_on_transfermarket_button_x, list_on_transfermarket_button_y)

                        time.sleep(get_random_time())

                        set_bid_price_button_x = 1320
                        set_bid_price_button_y = 665

                        pyautogui.click(set_bid_price_button_x, set_bid_price_button_y)
                        set_bid_price = int(list_player_price) - 100
                        pyautogui.typewrite(str(set_bid_price))

                        time.sleep(get_random_time())

                        set_price_item_button_x = 1320
                        set_price_item_button_y = 750
                        pyautogui.click(set_price_item_button_x, set_price_item_button_y)
                        pyautogui.typewrite(list_player_price)

                        time.sleep(get_random_time())

                        list_item_button_x = 1320
                        list_item_button_y = 870
                        pyautogui.click(list_item_button_x, list_item_button_y)

                        time.sleep(3)
                
                time.sleep(get_random_time())

                pyautogui.click(go_back_button_x, go_back_button_y)

                time.sleep(1)

                center_x, center_y = (1920 // 2, 1080 // 2)
                rec_x, rec_y = (center_x, center_y + 100)

                check_bid_price = pyautogui.screenshot(region=(rec_x - 400, rec_y - 100, 100, 300))
                check_bid_price.save("assets/check_bid_price.png")

                ocr_result2 = pytesseract.image_to_string("assets/check_bid_price.png", config = "--psm 6")

                if "150" in ocr_result2:
                    print("150 is in ocr res2")
                    pyautogui.click(minus_button_x, minus_button_y)
                else:
                    print("150 is not in ocr res2") 
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

        print("minimizing the browser for looking at the results...")

        browser.minimize()

        return """<div class="bg-green-500 text-white p-4">[SUCCESS] - The program has been executed successfully.</div>"""


    return """<div class="bg-red-500 text-white p-4">[ERROR] - Please open the FC Ultimate Team Web App and try again.</div>"""