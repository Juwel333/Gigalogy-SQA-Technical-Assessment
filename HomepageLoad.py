import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo-shop.gigalogy.com.bd/")
time.sleep(5)
#To click skip button
driver.find_element(By.CSS_SELECTOR, "#headlessui-dialog-panel-\:r1\: > article > div > article > div > div.absolute.inset-0.flex.flex-col.items-center.justify-center.p-4.top-\[66\%\].md\:top-\[10\%\].md\:rounded-xl > div > button:nth-child(1)").click()
time.sleep(5)

company_title = driver.title
print("Company Title:", company_title)

driver.close()
driver.quit()