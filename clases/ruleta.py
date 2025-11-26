
import random
#from clases.casillas import Casillas | mas adelante voy a necesitar intanciar la clase

class Ruleta(): #Clase con la que se va a crear el objeto Ruleta luego

    def __init__(self):
        self.__lista_de_casillas: list[Casillas] = [] #Aca encapsulamos en una lista las casillas

    def agregar_casilla(self, casilla: Casillas) -> None: #Esta funcion añade una casilla a la ruleta
        self.__lista_de_casillas.append(casilla)

    def _ordenar_casillas(self) -> None: #Aca utilizamos el random para mezclar las casillas de manera azárica
        random.shuffle(self.__lista_de_casillas)



    