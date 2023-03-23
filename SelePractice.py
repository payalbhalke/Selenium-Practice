import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(15)
# title
driver.get("https://www.makemytrip.com/")
time.sleep(10)

# Select Language
driver.find_element(By.XPATH,'//span[@class="switcherDownArrow appendLeft10"]').click()
radios = driver.find_elements(By.XPATH, '//div[@class="radioOuter"]/label')
for radio in radios:
    if radio.text == "English":
        radio.click()
        break

# selecting elements on web page like hotels and so on

driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()
lists = driver.find_elements(By.XPATH, "//div/a/span[@class='chNavText darkGreyText']")
print(lists)
for list in lists:
    if list.text == "Hotels":
        list.click()
        print(list)
        break




























