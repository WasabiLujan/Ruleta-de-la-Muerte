from casillas import Casillas

def CasillaMorir(Casillas):

    def __init__(self, puntos:int = 0):
        super().__init__(puntos)

    def mostrar_puntos(self) -> None:
        print("¡Oh no! Casilla de Muerte. Adiós puntos, Haz morido.")

    def aplicar_efecto(self, puntos_actuales:int) -> int:
        return 0