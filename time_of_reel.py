from login import driver, time
from login import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.instagram.com/reel/C34GR0Co3lU/"

driver.get(link)

time_of_upload = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//time[@class='x1p4m5qa']")))

print(time_of_upload.text)


input("Press Enter to close the browser...")
driver.quit()