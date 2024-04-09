# Importar las clases necesarias
from error import Error
from anuncio import Video, Social, Display
from datetime import datetime

# Definir la clase Campania
class Campania():
    def __init__(self, nombre: str, fecha_inicio: datetime,
            fecha_termino: datetime, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios 

    def __str__(self):
        cantidad_video = 0
        cantidad_display = 0
        cantidad_social = 0

        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cantidad_video +=1
            elif isinstance(elemento, Display):
                cantidad_display +=1
            elif isinstance(elemento, Social):
                cantidad_social +=1


        return f"""
        Nombre de la Campaña: {self.__nombre}
        Anuncios:{cantidad_video} Video, {cantidad_display} Display, {cantidad_social} Social
        """
        # Inicializa la campania con nombre, fechas de inicio y termino, y una lista de anuncios

    # Método para obtener la instancia del tipo correcto de anuncio
    def __obtener_instancia_anuncio(self, anuncio: dict):
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)

    # Método de propiedad para acceder al nombre de la campania
    @property
    def nombre(self) -> str:
        return self.__nombre

    # Método setter para el nombre de la campania y que no supere los 250 caracteres
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            print("Error: Nombre excede los 250 caracteres")

    # Método de propiedad para acceder a la fecha de inicio
    @property
    def fecha_inicio(self) -> datetime:
        return self.__fecha_inicio

    # Método setter para la fecha de inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: datetime) -> None:
        self.__fecha_inicio = fecha_inicio

    # Método de propiedad para acceder a la fecha de término
    @property
    def fecha_termino(self) -> datetime:
        return self.__fecha_termino

    # Método setter para la fecha de término
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino: datetime) -> None:
        self.__fecha_termino = fecha_termino

    # Método de propiedad para acceder a la lista de anuncios
    @property
    def anuncios(self) -> list:
        return self.__anuncios
    
    @anuncios.setter
    def anuncios(self, anuncios: list) -> None:
        self.__anuncios = anuncios

    # Método para obtener una representación en cadena de la campania
    def __str__(self):
        cant_video = len(list(filter(
            lambda x: isinstance(x, Video), self.anuncios
        )))
        cant_display = len(list(filter(
            lambda x: isinstance(x, Display), self.anuncios
        )))
        cant_social = len(list(filter(
            lambda x: isinstance(x, Social), self.anuncios
        )))

        return (f"Nombre de la Campania: {self.__nombre}\n"
                f"Anuncios: {cant_video} Video, "
                f"{cant_display} Display, "
                f"{cant_social} Social")