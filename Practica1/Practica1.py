import math
import random
import matplotlib.pyplot as plt
import time
import sys

class Combinacion:
    """Creates an object that will store all the caracteristics of the combinations"""
    def __init__(self, combinacion, numero_de_1, largo):
        self.numero = combinacion
        self.numero_de_1 = numero_de_1
        self.largo = largo
 
def contador(numero):
    """Function that will return how many oones an combination has"""
    unos = 0
    for i in numero:
        unos += int(i)
    return unos
 
def longitud(string):
    """Function that return the lenght of a given string"""
    lon = 0
    for i in string:
        if i != "\n" or i != "\0":
            lon += 1
    return lon
 
def bina(decimal):
    """Transform an decimal value into an binary string"""
        
    binario = str(bin(decimal))[2:]
    unos = contador(binario)
    
    return Combinacion(binario, unos, longitud(binario))

def ingerir(unos, largo):
    """Create various graphics"""
    
    graficar(unos, "Combinaciones posibles", "# de unos")
    graficar(largo, "Combinaciones posibles", "# de digitos")
    
    graficar(logrec(unos), "Combinaciones posibles log10", "# de unos")
    graficar(logrec(largo), "Combinaciones posibles log10", "# de digitos")
    
def logrec(array):
    """Reads an string and calculate log10 of every element"""
    aux=[]
    for i in array:
        if i == 0:
            #If log gets an 0 or less, then we will get an math error
            pass
        else:
            aux.append(math.log10(int(i)))
    return aux
    
def graficar(y_axis, titlex, titley):
    """Function to create a graph"""
    try:
        inicio = time.time()
        ax = plt.subplot()
        plt.xlabel(titlex)
        ax.set_yscale('log')
        plt.ylabel(titley)
        plt.title(titlex + " y "+titley)
        ax.plot(y_axis)
        fin = time.time()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        
    except (KeyboardInterrupt, BufferError):
        fin = time.time()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        

if __name__ == "__main__":
    """Main function"""
    while True:
        print("1) Realizar un nuevo calculo del universo")
        print("2) Salir")
        opc = int(input("Seleccione una opcion: "))
        
        if opc == 1:
            print("\n")
            print("1) Modo manual: ")
            print("2) Modo automatico: ")
            aux = int(input("Seleccione una opcion: "))
            
            if aux == 1:
                n = int(input("\nIntroduce n, no mayor a 1000 ni menor a 0: "))
                if 1000 < n < 0:
                    print("Error, el numero introducido no es valido")
                    break
            
            elif aux ==2:
                n = random.randint(1,1000)
            
            else:
                print("Error, seleccione una opcion correcta")
                break
            
            lim = pow(2, n)
            unos = []
            largo = []
            
            filec = open("resultados.txt", "w")
            filec.write('Σ^* = { ε, \n')
            
            inicio = time.time()
            for i in range (lim):
                try:
                    cadena = bina(i)
                    filec.write(str(cadena.numero)+",\n")
                    unos.append(cadena.numero_de_1)
                    largo.append(cadena.largo)
                    del cadena
                    
                except (KeyboardInterrupt, BufferError):
                    break

            filec.write("}")
            fin = time.time()
            filec.close()
            print(sys.getsizeof(unos))
            print(sys.getsizeof(largo))
            print("El tiempo de ejecucion para n = "+str(n)+" es: "+str(fin-inicio))
            del inicio
            del fin
            del aux
            del opc
            del n
            ingerir(unos, largo)
            
            
        elif opc == 2:
            exit()
        
        else:
            print("Error, seleccione una opcion correcta\n")