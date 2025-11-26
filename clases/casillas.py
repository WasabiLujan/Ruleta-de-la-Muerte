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

from clases.casillas import Casillas

class CasillaWin(Casillas):

    def __init__(self, puntos:int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"Ganaste {self.get_puntos()} puntos!")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return puntos_actuales + self.get_puntos()

from clases.casillas import Casillas

class CasillaMorir(Casillas):

    def __init__(self, puntos:int = 0):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print("¡Oh no! Casilla de Muerte. Adiós puntos, Haz morido.")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return 0


from clases.casillas import Casillas

class CasillaLose(Casillas):

    def __init__(self, puntos:int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"Perdiste {self.get_puntos()} puntos!")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return max(0, puntos_actuales - self.get_puntos())