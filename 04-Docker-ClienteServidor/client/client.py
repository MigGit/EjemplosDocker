import time
import requests

time.sleep(5)  # Da tiempo a que el contenedor de la API arranque

response = requests.get("http://app:5000/saludo")
print("Respuesta desde la API:", response.json())
