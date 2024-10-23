from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

# Navegacion hacia un URL
driver.get("https://www.google.com")
print(driver.title)
time.sleep(25)

