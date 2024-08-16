from login import driver, time
from login import By
from read_txt import read_text
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

links = read_text().split('\n')
print("Links:", links)

def convert_text_to_number(text):
    text = text.strip()  
    if text:
        if 'K' in text:
            number = float(re.search(r'\d*\.?\d+', text).group())
            return int(number * 1000)
        elif 'M' in text:
            number = float(re.search(r'\d*\.?\d+', text).group())
            return int(number * 1000000)
        else:
            try:
                return int(text.replace(',', ''))
            except ValueError:
                return 0  # Return 0 if conversion fails
    else:
        return 0  # Return 0 if text is empty


with open('view_counts.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
# Loop through each link
    for idx, content in enumerate(links):
        print(f"index value of {idx}")

        try:
        # WebDriver initialization and other setup code here

            driver.get(content) 
            time.sleep(3)
            print("Opening link:", content)
            time.sleep(3)  

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class ='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aa-z _ap3g _a6hd']"))
            )
            # Click on the element
            element.click()

            time.sleep(4)
            print("Scroll is starting")
            # increase scroll time later
            scroll_duration = 8 
            scroll_interval = 4
            total_scroll_time = 0

            # scrolling starts here
            while total_scroll_time < scroll_duration:
                time.sleep(4)
                driver.execute_script("window.scrollBy(0,1000);")
                total_scroll_time += scroll_interval
                print("Scrolling...")
                
            print("Scroll done")

            print("ok1")

            child_divs = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH,"//div[@class ='_aajy']//span[@class = 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']"))
            )
            time.sleep(3)

            view_counts = []

            for child_div in child_divs:
                value = child_div.text.strip()
                print("value", value)
                # print(type(value))
                processed = convert_text_to_number(value)
                print(processed)
                view_counts.append(processed)

            total_views = sum(view_counts)
            print("total sum for a reel", total_views) 
            csv_writer.writerow([content, total_views])
            print(f"Append complete, link is {content} and view counts is {total_views}")
            print(".......................................")

        
        except TimeoutException as e:
            print(f"Timeout error occurred for link {content}: {str(e)}")
        except Exception as e:
            print(f"An error occurred for link {content}: {str(e)}")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")
driver.quit()