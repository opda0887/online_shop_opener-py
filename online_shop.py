# 商品查詢器~
from selenium import webdriver
import pyautogui
# edge 的 webdriver 要依照版本來做更新！！

def OpenDriver():
    # executable_path 因人而異，請注意!!
    driver = webdriver.Edge(executable_path="X:\\edge_driver\\msedgedriver.exe")
    driver.maximize_window
    return driver

# ----------------------------------------------------------
#                        Main program
# ----------------------------------------------------------
# 讓使用者輸入他要查的東西
print("----------")
want = input("欲查詢的商品：")

if (want.replace(" ", "") != ""):

    money_range = input("是否要開啟價格範圍(填入\"是\" or \"否\")：")
    if money_range == "是":
        miniprice = input("所需的最<低>價位：")
        maxprice = input("所需的最<高>價位：")
    elif money_range == "否":
        #　不會做任何事
        skip = 1 
    else :
        print("所輸入的方式有誤-視為 \"否\" 來查找商品")

    store = input("欲在哪裡搜尋{ 1.蝦皮、2.momo、3.露天、4.Amazon(無價格範圍)、5.以上四者皆要 } --- 輸入編號：")

    if (store == "1") or (store == "1."):
        if money_range == "否" or money_range != "是":
            if (money_range != "是" and money_range != "否"):
                print("所請求的方式不對，但仍幫你查找商品")
            OpenDriver().get(f"https://shopee.tw/search?keyword={want}")
        else:
            OpenDriver().get(f"https://shopee.tw/search?keyword={want}&maxPrice={maxprice}&minPrice={miniprice}")
        print("已成功協助搜尋")

    elif (store == "2") or (store == "2."):
        if money_range == "否" or money_range != "是":
            if (money_range != "是" and money_range != "否"):
                print("所請求的方式不對，但仍幫你查找商品")
            OpenDriver().get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}")
        else:
            OpenDriver().get(f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={want}&_advPriceS={miniprice}&_advPriceE={maxprice}")
        print("已成功協助搜尋")

    elif (store == "3") or (store == "3."):
        if money_range == "否" or money_range != "是":
            if (money_range != "是" and money_range != "否"):
                print("所請求的方式不對，但仍幫你查找商品")
            OpenDriver().get(f"https://www.ruten.com.tw/find/?q={want}")
        else:
            OpenDriver().get(f"https://www.ruten.com.tw/find/?q={want}&prc.now={miniprice}-{maxprice}")
        print("已成功協助搜尋")

    elif (store == "4") or (store == "4."):
        if money_range == "是":
            print("目前沒有價格查詢功能，但仍幫你查找商品")
        elif money_range != "否":
            print("所請求的方式不對，但仍幫你查找商品")
        OpenDriver().get(f"https://www.amazon.com/s?k={want}")
        print("已成功協助搜尋")

    elif (store == "5") or (store == "5."):
        page = 1
        driver = OpenDriver()
        
        if money_range == "否":
            driver.get(f"https://shopee.tw/search?keyword={want}")

            #[1]：按下 Ctrl + T 來新增分頁，而且要搭配pyautogui
            pyautogui.hotkey('ctrl', 't', interval=0.1) #[1]
            #[2]：切換瀏覽器的window handle
            driver.switch_to.window(driver.window_handles[page]) #[2]
            #[3]：page記得+1
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
        elif money_range == "是":
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
        print("已成功協助搜尋")
    else :
        print("目前無提供此類商城來搜尋，或者是您的輸入有誤~")

elif (want.replace(" ", "") == ""):
    print("! 您的輸入方式有誤 !")

print("----------")