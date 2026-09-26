import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.support.wait import WebDriverWait
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
search_box = driver.find_element(By.ID,"search").send_keys("「To b. by agnes b.」 2WAYバッグ - ブラック レディース")
time.sleep(10)
# Locate the Search button and click
search_button = driver.find_element(By.XPATH,'//div[contains(@class, "bg-accent") and normalize-space()="Search"]').click()
time.sleep(10)
# Locate and click the first product from the search results
# This waits until the product is clickable
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/main/div/div/div[4]/div/div[1]/article[1]'))).click()
time.sleep(5)
#Located and Click for Add to card product
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/div[2]/article/article/div[1]/div[2]/div[1]/div[3]/div/div[1]').click()
time.sleep(5)
# Get the product name from the Product Details page
product_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH,'//*[@id="headlessui-dialog-panel-:r3:"]'))).text
# Close the current browser window
driver.close()
# Close all browser windows
driver.quit()
