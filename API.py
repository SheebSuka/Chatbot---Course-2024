# Importaciones de librerias
from openai import OpenAI
import os

# Definicion de cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    max_tokens=0.2,
    messages=[
        {"role": "system", "content": '''
            "Eres un profesor de Ing. En Software en la universidad Estatal de Sonora, solo responder UNICAMENTE preguntas relacionadas al contenido":
            1.- Materia Optativa de FrontEnd, url://www.ues.mx, dia: Lunes a Viernes
            2.- Materia Programación Web, url: https://www.ues.mx, dia: Martes, Jueves
            3.- Inteligencia Artificial, url://https:www.ues.mx, dias: Lunes a Vierens'''},
        {"role": "user", "content": "¿Hola, buenas tardes?"},
        {"role": "user", "content": "¿Tienen cursos los dias sabados?"},
        {"role": "user", "content": "Los Dias sabados, solamente se atienden actividades extracurriculares"},
        {"role": "user", "content": "¿Las actividades extra curriculares, tienen costo?"},
    ]
)

# Enviamos a impresión
print(response)
