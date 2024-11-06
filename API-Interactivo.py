# Importaciones de librerias
from openai import OpenAI
import os

# Definicion de cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)


# Mensajes
messages = [
    {"role": "system", "content": '''
            "Eres un profesor de Ing. En Software en la universidad Estatal de Sonora, solo responder UNICAMENTE preguntas relacionadas al contenido":
            1.- Materia Optativa de FrontEnd, url://www.ues.mx, dia: Lunes a Viernes
            2.- Materia Programación Web, url: https://www.ues.mx, dia: Martes, Jueves
            3.- Inteligencia Artificial, url://https:www.ues.mx, dias: Lunes a Vierens'''}
]

# Interactividad
user_message = ''

# Declaramos bucle
while (user_message != 'exit'):
    # Cargar mensaje del ususario en la variable
    print("Redactar mensaje ususario")
    user_message = input()

    # Manejo del historial y los mensajes
    if len(messages) >= 1 and len(messages) <= 4:
        messages.append({'role': 'user', 'content': user_message})
    else:
        # Colocamos bucle FOR
        for i in range(3, len(messages), 2):
            messages[i-2] = messages = [i]
            messages[i-1] = messages[i+1]
        messages[len(messages)-2] = {'role': 'user', 'content': user_message}
        messages.pop

    # Establecemos la respuesta
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0.2,
        messages=messages
    )
    assistance_message = response.choices[0].message.content
    print(f"LA API responde de la siguiente manera --> {assistance_message}")

    # Despues de la llamada de la API
    print("Despues de haber llamad a la api tenemos la sig respuesta --> ")
    print(messages)
