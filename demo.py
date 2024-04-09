from campaña import Campania
from datetime import datetime

# Creación de una instancia de Campania y definición de sus atributos
c = Campania("Campania Demo", datetime.today(), datetime.today(), [
    {"tipo": "video", "url_clic": "sin-url", "url_archivo": "sin-url",
    "sub_tipo": "instream", "duracion": 30}
])

try:
    # Solicita al usuario ingresar un nuevo nombre para la campaña
    nombre = input("Ingrese nuevo nombre de la campania:\n")
    # Solicita al usuario ingresar un nuevo subtipo para el anuncio
    sub_tipo = input("Ingrese nuevo sub tipo del anuncio:\n")

    # Actualiza el nombre de la campaña
    c.nombre = nombre
    # Actualiza el subtipo del primer anuncio en la lista de anuncios
    c.anuncios[0].sub_tipo = sub_tipo

except Exception as e:
    # Manejo de excepciones: si ocurre algún error, se registra en el archivo error.log
    with open("error.log", "a+", encoding="utf-8") as log:
        # Escribe el error en el archivo de registro
        log.write(f"{e}\n")

print(c)
