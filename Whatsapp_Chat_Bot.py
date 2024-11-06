# Se requiere importar las siguientes librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Importamos modulos adicionales
from openai import OpenAI
import os

# Crecion cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)


def call_endpoint(messages):
    chatgpt_messages_list = [
        {"role": "system", "content": '''
         Eres un programador Senior en una empresa reconocida, solamente y UNICAMENTE debes de contestar contenido relacionado al siguiente contenido:
         Mi correo es: franciscoscaraveor@gmail.com
         1.- Desarollador en Javascript, Experencia: 5 años.
         2.- Programador FullStack, Experencia 3 años.
         3.-
         '''}
    ]
    chatgpt_response = chatgpt_messages_list + messages
    # Se genera la respuesta
    chatgpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=messages
    )

    assistance_message = chatgpt_response.choices[0].message.content

    return assistance_message


# Colocaremos las opciones
options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\santy\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

# Asignaremos las opciones como argumento
driver = webdriver.Chrome(options=options)

# Establecemos las dimensiones de la venta
driver.set_window_size(1024, 720)
driver.set_window_position(0, 0)

# Implementamos
driver.implicitly_wait(3600)
driver.get("https://web.whatsapp.com/")

while (True):
    # Expresiones xPad
    # //*[@id="pane-side"]/descendant::span[contains(@aria-label,'no leídos')]
    # //*[@id="main"]/descendant::div[@role='row']
    # //div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span
    # //*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]

    # Recuperamos nuevos mensajes
    new_message = driver.find_element(
        By.XPATH, '//*[@id="pane-side"]/descendant::span[contains(@aria-label,\'unread\')]')
    new_message.click()

    # Obtener los mensajes del usuario
    last_messages = driver.find_elements(
        By.XPATH, '//*[@id="main"]/descendant::div[@role=\'row\']')
    last_message = last_messages[-1]

    # Enviamos a impresion el mensaje que hemos seleccionado
    last_message_text = last_message.find_element(
        By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span').text
    print(f'user message:{last_message.text}')

    # Establecemos una lista
    message_list = []
    message_list.append({'role': 'user', 'content': last_message_text})

    # Notificar al usuario, que se envia el texto
    print('sending message to lenguaje service')
    # Simulacion de API
    # api_message = "Alivianese o la meo <-- Att: Chatbot ñejeje"

    api_message = call_endpoint(message_list)

    message_element = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    message_element.send_keys(f'{api_message}{Keys.ENTER}')
    message_element.send_keys(Keys.ESCAPE)
