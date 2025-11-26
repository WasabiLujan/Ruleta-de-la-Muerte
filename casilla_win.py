from casillas import Casillas

class CasillaWin(Casillas):

    def __init__(self, puntos:int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"Ganaste {self.get_puntos()} puntos!")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return puntos_actuales + self.get_puntos()