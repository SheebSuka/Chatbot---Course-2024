# IMPORTACION DE BIBLIOT4ECAS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Instanciar y vamos a dimensionar
driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(1024, 720)

# Solicitar una URL
driver.get('https://courses.academti.com/chatbot/weather-stations/add?authuser=0')
time.sleep(3)

# Crearemos un diccionar KEY, VALUE
# nombre_diccionario={ 'kay': 'value'}
station_row = {
    'ID': 'AEM00041216',
    'Station Name': 'ABU_DHABI_BATEEN_AIR',
    'Elev-m': '3',
    'Lat': '24.43',
    'Lon': '54.47',
    'Type': 'Semiautomatic',
    'Temperature': '0',
    'Atmospheric_Pressure': '1',
    'Humidity': '0',
    'Precipitation': '1',
    'Radiation': '1'
}

# Se declaran variables a las que asignaremos al diccionario asociando al valor po rmedio de la llave.
station_id = station_row['ID']
station_name = station_row['Station Name']
station_elevm = station_row['Elev-m']
station_lat = station_row['Lat']
station_lon = station_row['Lon']
station_type = station_row['Type']
station_temp = station_row['Temperature']
station_at_pre = station_row['Atmospheric_Pressure']
station_humidity = station_row['Humidity']
station_precipitation = station_row['Precipitation']
station_radiation = station_row['Radiation']

# Nombre de los controles en el formulario
# ID = stationId
# Station_name = stationName
# Elevacion = number
# Latitudi = coordinate
# Logitud = coordinate [0],[1]

# Declaramos variables
# Recueramos y enviamos el indentificador
station_id_element = driver.find_element(By.ID, 'stationId')
station_id_element.send_keys(station_id)
time.sleep(0.2)

# Recuperamos y enviamos el nombre
station_name_element = driver.find_element(By.NAME, 'stationName')
station_name_element.send_keys(station_name)
time.sleep(0.2)

# Recuperamos yu enviamos el valor de elevacion
station_elevation_element = driver.find_element(By.CLASS_NAME, 'number')
station_elevation_element.send_keys(station_elevm)
time.sleep(0.2)

# Recuperamos y enviamos la latitud y la longitud
station_element = driver.find_elements(By.CLASS_NAME, 'coordinate')
station_element[0].send_keys(str(station_lat))
station_element[1].send_keys(str(station_lon))
time.sleep(10)
