from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Navegacion hacia pagina de Whatsapp
driver.get("https://web.whatsapp.com/")
print(driver.title)
time.sleep(5)


# Navegacion hacia un URL
driver.get("https://www.google.com")
print(driver.title)
time.sleep(5)

#Back METHOD
driver.back()
print(driver.current_url)
time.sleep(5)

#Foward Method
driver.forward()
print(driver.current_url)
time.sleep(5)


