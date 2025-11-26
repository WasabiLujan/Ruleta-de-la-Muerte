from abc import ABC, abstractmethod

class Casillas(ABC):

    def __init__(self, puntos:int):
        self.__puntos_de_casilla = puntos

    def get_puntos(self) -> int:
        return self.__puntos_de_casilla

    @abstractmethod
    def mostrar_puntos(self) -> None:
        pass

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        pass