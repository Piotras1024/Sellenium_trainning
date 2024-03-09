from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

url = "https://www.google.com/"

# uruchomienie konkretnego adresu
driver.get(url)

# zaakceptuj zgody
accept_button = driver.find_element("id", "L2AGLb")
accept_button.click()

# Wpisz "szukam Cie" w polu wyszukiwania
search = driver.find_element('name', 'q')
search.send_keys("Szukam Cie")
time.sleep(3)

# Wyślij zapytanie wyszukiwania
# search.submit() wykonaj akcje
search.send_keys(Keys.ENTER)
time.sleep(3)


# zamknięcie przeglądarki -> jak zamknięcie poprzez X
driver.quit()

