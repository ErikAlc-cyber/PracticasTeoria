import random

"""
Usar el sistema de tabla:
Ficha 1: numeros grandes
Ficha 2: Numeros >= a inicio
Matar una casilla = o
Si estado e instuccion son = entonces buscar diagonalmente
Por el contrario buscar recto, excepto casilla este muerta

"""

jug = []
class ficha:
    def __init__(self, inicio, fin, actual):
        self.inicio = inicio
        self.fin = fin
        self.actual = actual
        self.ruta = ""
    
    def new_rute(self,ruta):
        self.ruta = ruta

def tablero():
    Dimensiones = 4
    for i in range(Dimensiones):
        if(i % 2 == 0 or i == 0):
            alt1 = "rojo"
            alt2 = "negro"
        else:
            alt1 = "negro"
            alt2 = "rojo"
        for j in range(Dimensiones):
            if(j % 2 == 0 or j == 0):
                print("La casilla es " + alt1)
            else:
                print("La casilla es " + alt2)
    
        

def iniciorand():
    a = random.randint(1,10)
    if(a % 2 == 0):
        print("Inicia Blanco")
    else:
        print("Inicia Negra")

def randomInst(num):
    aux = "";
    for i in range(num):
        a = random.randint(1,10);
        if(a % 2 == 0):
            aux = aux + "r"
        else:
            aux = aux + "b"
    return aux
    
def Jugadores(num):
    global jug
    for i in range(num):
        cadena = input("Introduce una cadena de instrucciones o el numero de movimientos que debe realizar el jugador "+str(i+1)+" :")   
        if(i % 2 == 0):
            jug.append(ficha(0,16,0))
        else:
            jug.append(ficha(4,13,0))

        if (cadena.isdigit()):
            aux = int(cadena)
            instrucciones = randomInst(aux)
        else:
            instrucciones = cadena
        jug[i].new_rute(instrucciones)
    inicio = iniciorand()

if __name__ == "__main__":
    """Main function"""
    
    while(True):
        print("Menu de opciones")
        print("1) Manual")
        print("2) Automatico")
        print("3) Salir")
        opc = int(input("Que modo va a ser?:"))
        if (opc == 1):
            jugadores = int(input("Cuantos jugadores tendran el juego?:"))
            Jugadores(jugadores)
            #tablero()
        elif (opc == 2):
            print("Automatico")
        elif (opc == 3):
            exit()