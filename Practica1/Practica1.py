import math
import matplotlib.pyplot as plt
import time
import sys

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

def ingerir(unos, largo):
    """Create various grafics"""
    
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
    print("Welcome to python baby")
