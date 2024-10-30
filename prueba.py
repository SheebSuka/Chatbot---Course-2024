from selenium import webdriver
import time


# Ejecutamos las opciones
options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\santy\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


driver = webdriver.Chrome(options=options)

# Tamaño vetnatan
driver.set_window_size(1024, 720)
driver.set_window_position(0, 0)

driver.get("https://web.whatsapp.com/")

time.sleep(3600)

# //*[@id="pane-side"]/descendant::span[contains(@aria-label,'Unread')]
# //*[@id="main"]/descendant::div[@role='row']
#//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span
#//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]
