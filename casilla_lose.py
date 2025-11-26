from casillas import Casillas

class CasillaLose(Casillas):

    def __init__(self, puntos:int):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print(f"Perdiste {self.get_puntos()} puntos!")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return max(0, puntos_actuales - self.get_puntos())
