
from login import driver, time
from login import By
from read_txt import read_text
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd

links = read_text().split('\n')
print("Links:", links)

data = []

for content in links:
    try:
        driver.get(content) 
        time.sleep(3)
        print("Opening link:", content)
        time.sleep(2)  

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class ='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aa-z _ap3g _a6hd']"))
        )
        element.click()

        time.sleep(4)
        print("Scroll is starting")
        scroll_duration = 6 
        scroll_interval = 4
        total_scroll_time = 0

        while total_scroll_time < scroll_duration:
            time.sleep(4)
            driver.execute_script("window.scrollBy(0,1000);")
            total_scroll_time += scroll_interval
            print("Scrolling...")
            
        print("Scroll done")

        view_counts = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//div[@class ='_aajy']//span[@class = 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']"))
        )

        reel_count =[]
        for x in view_counts:
            value = x.text
            reel_count.append(value)
            print("count of views",x.text)

        child_divs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='x1qjc9v5 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xdt5ytf x2lah0s xln7xf2 xk390pu xdj266r xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x11njtxf xpzaatj xw3qccf']//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']"))
        )

        for child_div, count in zip(child_divs, reel_count):
            href_value = child_div.get_attribute("href")
            data.append([content, href_value, count])
            print("Href/Reel link:", href_value)
            print("View count:", count)

        print(".......................................")
    
    except TimeoutException as e:
        print(f"Timeout error occurred for link {content}: {str(e)}")
    except Exception as e:
        print(f"An error occurred for link {content}: {str(e)}")

if data:
    df = pd.DataFrame(data, columns=["account_link", "reel_link", "views"])
    df.to_excel("Account_reels_links.xlsx", index=False)
else:
    print("No data to save.")
