# Products searcher~
from selenium import webdriver
import pyautogui
# edge's webdriver need to update with version！！

def OpenDriver():
    # executable_path varies from person to person!!
    driver = webdriver.Edge(executable_path="X:\\edge_driver\\msedgedriver.exe")
    driver.maximize_window
    return driver

def Error(type):
    if (type == "Input"):
        print("Input Error, but still help tou to find products.")
    elif (type == "Shop"):
        print("There is currently no such online shop to search, or your input is wrong~")
    else:
        print("! Error !")


# ----------------------------------------------------------
#                        Main program
# ----------------------------------------------------------
# Let user input what they want.
print("----------")
want = input("Want to find... ：")

if (want.replace(" ", "") != ""):

    money_range = input("Whether to open the price range(input \"y\" or \"n\" )：")
    checkYsame = money_range == "y" or money_range == "Y"
    checkNsame = money_range == "n" or money_range == "N"
    checkYnt = money_range != "y" and money_range != "Y"
    checkNnt = money_range != "n" and money_range != "N"

    if checkYsame:
        miniprice = input("The lowest price you want... ：")
        maxprice = input("The highest price you want... ：")
    elif checkNsame:
        #　Won't do anything.
        skip = 1 
    else :
        print("Input Error - seems \"n\" to find products.")

    store = input("Want to search in... { 1.shopee、2.momo、3.ruten、4.Amazon(no price range)、5.Above of all } --- input serial number：")

    if (store == "1") or (store == "1."):
        driver = OpenDriver()
        if checkNsame or checkYnt:
            if (checkYnt and checkNnt):
                Error("Input")
            driver.get(f"https://shopee.tw/search?keyword={want}")
        else:
            driver.get(f"https://shopee.tw/search?keyword={want}&maxPrice={maxprice}&minPrice={miniprice}")
        print("Succeed")

    elif (store == "2") or (store == "2."):
        driver = OpenDriver()
        if checkNsame or checkYnt:
            if (checkYnt and checkNnt):
                Error("Input")
            driver.get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}")
        else:
            driver.get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}&_advPriceS={miniprice}&_advPriceE={maxprice}")
        print("Succeed")

    elif (store == "3") or (store == "3."):
        driver = OpenDriver()
        if checkNsame or checkYnt:
            if (checkYnt and checkNnt):
                Error("Input")
            driver.get(f"https://www.ruten.com.tw/find/?q={want}")
        else:
            driver.get(f"https://www.ruten.com.tw/find/?q={want}&prc.now={miniprice}-{maxprice}")
        print("Succeed")

    elif (store == "4") or (store == "4."):
        driver = OpenDriver()
        if checkYsame:
            print("There is currently no price query function, but it still helps you find products.")
        elif checkNnt:
            Error("Input")
        driver.get(f"https://www.amazon.com/s?k={want}")
        print("Succeed")

    elif (store == "5") or (store == "5."):
        page = 1
        driver = OpenDriver()
        
        if checkNsame:
            driver.get(f"https://shopee.tw/search?keyword={want}")

            #[1]：click Ctrl + T to add new page
            pyautogui.hotkey('ctrl', 't', interval=0.1) #[1]
            #[2]：switch webdriver's window handle
            driver.switch_to.window(driver.window_handles[page]) #[2]
            #[3]：remind that: page+1
            page+=1 #[3]
            driver.get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}")

            pyautogui.hotkey('ctrl', 't', interval=0.1)
            driver.switch_to.window(driver.window_handles[page])
            page+=1
            driver.get(f"https://www.ruten.com.tw/find/?q={want}")
            
            pyautogui.hotkey('ctrl', 't', interval=0.1)
            driver.switch_to.window(driver.window_handles[page])
            page+=1
            driver.get(f"https://www.amazon.com/s?k={want}")

        elif checkYsame:
            driver.get(f"https://shopee.tw/search?keyword={want}&maxPrice={maxprice}&minPrice={miniprice}")
            
            pyautogui.hotkey('ctrl', 't', interval=0.1)
            driver.switch_to.window(driver.window_handles[page])
            page+=1
            driver.get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}&_advPriceS={miniprice}&_advPriceE={maxprice}")

            pyautogui.hotkey('ctrl', 't', interval=0.1)
            driver.switch_to.window(driver.window_handles[page])
            page+=1
            driver.get(f"https://www.ruten.com.tw/find/?q={want}&prc.now={miniprice}-{maxprice}")
            
            pyautogui.hotkey('ctrl', 't', interval=0.1)
            driver.switch_to.window(driver.window_handles[page])
            page+=1
            driver.get(f"https://www.amazon.com/s?k={want}")
        print("Succeed")
    else :
        Error("Shop")

elif (want.replace(" ", "") == ""):
    Error("")

print("----------")