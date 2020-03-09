# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Error Unicode equal comparison failed to convert both arguments to Unicode - interpreting
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')

# Session 1
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_experimental_option("prefs", {
    "download.default_directory": r"./",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://XXXXX.slack.com/services/export')

try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'email')))
except:
    print("Error : Can not loading page.")
print("Loading success #1")

email = driver.find_element_by_id('email')
email.clear()
email.send_keys('your email address')

password = driver.find_element_by_id('password')
password.clear()
password.send_keys('your password')

driver.find_element_by_id('signin_btn').click()

# Session 2
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'c-input_select__wrapper')))
except:
    print("Error : Can not loading page.")

print("Loading success #2")

range_input = driver.find_element_by_class_name(
    'c-input_select__wrapper')
range_input.click()
range_list = range_input.find_elements_by_tag_name('span')
for item in range_list:
    if item.text == '過去 30日間':
        item.click()
        break

driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/button').click()

print("Data exporting...")

# Session # 3
while 1:
    try:
        sleep(5)
        table = driver.find_element_by_id('export_history')
        tbody = table.find_element_by_tag_name('tbody')
        tr = tbody.find_elements_by_tag_name('tr')
        tr[0].find_elements_by_tag_name('a')[1].click()
        print("Export success")
        break
    except:
        driver.refresh()

print("File download finish")
# browser.close()
