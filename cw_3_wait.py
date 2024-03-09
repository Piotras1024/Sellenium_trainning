from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/")
search = driver.find_element('id', 'accept-choices')
search.click()

# wybranie menu "Tutorials"
menu = driver.find_element('id', 'navbtn_tutorials')
menu.click()



time.sleep(15)
driver.quit()

