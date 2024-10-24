#IMPORTACION DE BIBLIOT4ECAS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Instanciar y vamos a dimensionar
driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Solicitar una URL
driver.get('https://courses.academti.com/chatbot/weather-stations/add?authuser=0')
time.sleep(10)

#Crearemos un diccionar KEY, VALUE
#nombre_diccionario={ 'kay': 'value'}
station_row = {
    'ID':'AEM00041216',
    'Station Name':'ABU_DHABI_BATEEN_AIR',
    'Elev-m':'3',
    'Lat':'24.43',
    'Lon':'54.47',
    'Type:':'Semiautomatic',
    'Temperature':'0',
    'Atmospheric_Pressure':'1',
    'Humidity':'0',
    'Precipitation':'1',
    'Radiation':'1'
}