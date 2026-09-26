import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager

#Browser handle
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Navigate to the Url
driver.get("https://demo-shop.gigalogy.com.bd/")
# Waiting for website to load
time.sleep(5)
#To habdle the modal to click the skip button
driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/article/div/article/div/div[2]/div/button[1]').click()
time.sleep(5)
## Locate the search input field and enter the keyword for product search
search_box = driver.find_element(By.ID,"search").send_keys("ブレスレット AH71 BRACELET ブレスレット メンズ")
time.sleep(10)
# Locate the Search button and click
search_button = driver.find_element(By.XPATH,'//div[contains(@class, "bg-accent") and normalize-space()="Search"]').click()
time.sleep(5)

driver.close()
driver.quit()