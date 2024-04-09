# Importa la clase ABC y la función abstractmethod del módulo abc
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

# Definición de la clase Anuncio como clase abstracta
class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1 #se debe validar
        self.__alto = alto if alto > 0 else 1 #se debe validar
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__subtipo = sub_tipo

    # Método de propiedad para acceder al ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Método setter para el ancho
    @ancho.setter
    def ancho(self, ancho: int) -> None:
        self.__ancho = ancho if ancho > 0 else 1
    # Método de propiedad para acceder al alto
    @property
    def alto(self) -> int:
        return self.__alto

    # Método setter para el alto
    @alto.setter
    def alto(self, alto: int) -> None:
        self.__ancho = alto if alto > 0 else 1
    # Método de propiedad para acceder al url_archivo
    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    # Método setter para el url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo: str) -> None:
        self.__url_archivo = url_archivo
    # Método de propiedad para acceder al url_clic
    @property
    def url_clic(self) -> str:
        return self.__url_clic

    # Método setter para el url_clic
    @url_clic.setter
    def url_clic(self, url_clic: str) -> None:
         self.__url_clic = url_clic

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    # Método setter para el subtipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo

    # Método de propiedad para acceder al duracion
    @property
    def duracion(self) -> int:
        return self.__duracion

    # Método setter para el duracion
    @duracion.setter
    def duracion(self, duracion: int) -> None:
        self.__duracion = duracion

    @abstractmethod
    def comprimir_anuncios(self) -> None:  # Método abstracto para comprimir los anuncios
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:  # Método abstracto para redimensionar los anuncios
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")
    
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str, duracion:int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion >0 else 5
      

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self):
        pass

    def comprimir_anuncio(self):
        print("COMPRESION DE VIDEO NO IMPLEMENTADA AUN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AUN")

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self, ancho:int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESION ANUNCIO DISPLAY NO IMPLEMENTADO AUN")

    def redimensionar_anuncio(self):
        print("RECORTE ANUNCIO DISPLAY NO IMPLEMENTADO AUN")

class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")
    
    def __init__(self, ancho:int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESION ANUNCIO SOCIAL NO IMPLEMENTADO AUN")

    def redimensionar_anuncio(self):
        print("RECORTE ANUNCIO SOCIAL   NO IMPLEMENTADO AUN")


    @staticmethod
    def mostrar_formatos() -> None:  # Método estático para mostrar los formatos disponibles
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")
  
        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")




