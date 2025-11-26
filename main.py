import sys
import os 
from clases.usuario import Usuario
from clases.ruleta import Ruleta
from clases.casillas import CasillaWin, CasillaLose, CasillaMorir

class Game:
    """
    Clase orquestadora del juego, maneja el menú principal y el loop del juego.
    """
    def __init__(self):
        self.usuario: Usuario = None
        self.ruleta = Ruleta()

    def _limpiar_pantalla(self) -> None:
        """Detecta el sistema operativo y limpia la consola."""
        if os.name == 'nt': 
            os.system('cls')# para Windows
        else:
            os.system('clear')# para Mac

    def configurar_casillas(self) -> None:
        """Crea y agrega casillas variadas a la ruleta."""
        self.ruleta = Ruleta() 
        self.ruleta.agregar_casilla(CasillaWin(10))
        self.ruleta.agregar_casilla(CasillaWin(20))
        self.ruleta.agregar_casilla(CasillaLose(5))
        self.ruleta.agregar_casilla(CasillaLose(15))
        self.ruleta.agregar_casilla(CasillaMorir(0))
        self.ruleta.agregar_casilla(CasillaWin(50)) 

    def mostrar_logo(self) -> None:
        """Imprime el arte ASCII del título."""
        logo = r"""
  ____        _      _             _      _ 
 |  _ \ _   _| | ___| |_ __ _   __| | ___| |
 | |_) | | | | |/ _ \ __/ _` | / _` |/ _ \ |
 |  _ <| |_| | |  __/ || (_| || (_| |  __/ |
 |_| \_\\__,_|_|\___|\__\__,_| \__,_|\___|_|
   ____            _   _             
  |  _ \  ___  ___| |_(_)_ __   ___  
  | | | |/ _ \/ __| __| | '_ \ / _ \ 
  | |_| |  __/\__ \ |_| | | | | (_) |
  |____/ \___||___/\__|_|_| |_|\___/ 
        """
        print(logo)

    def mostrar_instrucciones(self) -> None:
        self._limpiar_pantalla() # <--- Limpia para empezar el juego limpio
        print("\n" + "="*40)
        print("     ░   INSTRUCCIONES DEL AVERNO ░ ")
        print("="*40)
        print("1. El objetivo es llegar a 100 puntos para salvarte.")
        print("2. Si tus puntos bajan a 0, mueres y pierdes.")
        print("3. Existen casillas de VICTORIA, DERROTA y MUERTE.")
        print("4. Confía en tu suerte... o en Thor.")
        print("="*40)
        input("\nPresiona ENTER para volver al menú...")

    def mostrar_creditos(self) -> None:
        """Team Carpigames."""
        self._limpiar_pantalla()          
        carpincho = r'''
           /"""""\
          /  o  o \      __  
         |    ^    |    /  |
         |   '-'   |   /   |
          \_______/___/   /
           |             |
           |  CARPIGAMES |
           |_____________|
        '''        
        print("\n" + "*"*40)
        print("       ░ CRÉDITOS DE DESARROLLO ░")
        print("*"*40)
        print(carpincho)
        print("\nDesarrollado por TEAM CARPIGAMES:")
        print("\n   > Michael")
        print("   > Cintia")
        print("   > Daniela")
        print("   > Lujan")
        print("\nGracias por jugar a nuestra creación.")
        print("*"*40)
        input("\nPresiona ENTER para volver al menú...")
    def iniciar_partida(self) -> None:
        self._limpiar_pantalla() 
        print("\n--- Preparando el tablero... ---")
        nombre = input("Ingresá tu nombre, jugador del caos: ")
        self.usuario = Usuario(nombre)
        self.configurar_casillas()

        # Limpiamos una vez más para que empiece el loop visualmente ordenado
        self._limpiar_pantalla() 
        print(f"Bienvenido, {nombre}. Tu destino comienza ahora.")

        while self.usuario.puntos_usuario >= 0 and self.usuario.puntos_usuario < 100:
            print(f"\n" + "-"*30)
            print(f"Estado actual: {self.usuario.puntos_usuario} puntos.")
            print("-"*30)
            
            input(f"--> {self.usuario.nombre_usuario}, presiona [ENTER] para girar la ruleta...")
            
            # Nota: en esta parte no limpiamos dentro del loop para que se pueda leer qué pasó en el turno anterior
            self.usuario.tirar_ruleta(self.ruleta)

            if self.usuario.puntos_usuario == 0:
                print("\n¡Game over! La muerte te reinició.")
                break
            elif self.usuario.puntos_usuario >= 100:
                print("\n¡Victoria! Alcanzaste la luz.")
                break
        
        input("\nPartida finalizada. Presiona ENTER para volver al menú principal...")

    def menu_principal(self) -> None:
        while True:
            self._limpiar_pantalla()
            self.mostrar_logo()
            print("\n1. ░ JUGAR")
            print("2. ░ INSTRUCCIONES")
            print("3. ░ CRÉDITOS")
            print("4. ░ SALIR")
            
            opcion = input("\nElige tu destino (1-4): ")

            if opcion == "1":
                self.iniciar_partida()
            elif opcion == "2":
                self.mostrar_instrucciones()
            elif opcion == "3":
                self.mostrar_creditos()
            elif opcion == "4":
                print("Huyendo tan pronto... ¡Adiós!")
                break
            else:                
                print("Opción incorrecta.")
                input("Presiona Enter para intentar de nuevo...")

if __name__ == "__main__":
    juego = Game()
    juego.menu_principal()