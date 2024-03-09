from selenium import webdriver
import time

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

url = "https://www.google.com/"
new_url = "https://www.wp.pl"

# uruchomienie konkretnego adresu
driver.get(url)

# otwórz nowe okno
driver.execute_script("window.open('');")

# Opcjonalnie: przełącz się na nową zakładkę, jeśli chcesz z niej korzystać
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)

# maksymalizacja okna
driver.maximize_window()

time.sleep(3)

driver.set_window_size(800, 400)

time.sleep(1)

# zamknięcie przeglądarki -> jak zamknięcie poprzez X
# driver.close() zamknięcie 1 okna.
driver.close()
time.sleep(1)
driver.quit()

