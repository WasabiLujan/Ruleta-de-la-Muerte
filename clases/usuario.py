import time
import sys
from clases.ruleta import Ruleta
from clases.casillas import Casillas

class Usuario:
    """
    Clase que representa al usuario, con nombre, puntos y lógica para interactuar con la ruleta.
    """
    def __init__(self, nombre: str):
        self.nombre_usuario = nombre
        self.puntos_usuario = 0  # Puntos iniciales

    def tirar_ruleta(self, ruleta: Ruleta) -> None:
        """Tira la ruleta, muestra animación y aplica efecto polimórfico."""
        
        # Animación de suspenso ASCII
        print(f"GIRANDO...", end=" ")
        simbolos = ['|', '/', '-', '\\']
        for _ in range(10):  # Cantidad de vueltas
            for simbolo in simbolos:
                sys.stdout.write(simbolo)
                sys.stdout.flush()
                time.sleep(0.06) # Velocidad
                sys.stdout.write('\b') # Borra el caracter anterior

        print(" ¡STOP!") # Fin de animación
        
        # (Polimorfismo)
        casilla: Casillas = ruleta.detenerse()
        casilla.mostrar_puntos()
        self.puntos_usuario = casilla.aplicar_efecto(self.puntos_usuario)
