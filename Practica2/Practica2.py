import random
from cupshelpers import Printer
import matplotlib.pyplot as plt
import itertools
import time
import math

#Mausque herramienta para mas tarde: liminf, limmed

def ingerir(unos, largo):
    """Create various graphics"""
    
    graficar(unos, "2^n", "# de unos")
    graficar(largo, "2^n", "# de digitos")
    graficar(logrec(unos), "2^n", "log10(# de unos)")
    graficar(logrec(largo), "2^n", "log10(# de digitos)")
    
def logrec(array):
    """Apply Log base 10 to every element in array"""
    aux=[]
    for i in array:
        aux.append(math.log10(int(i)))
    return aux

def graficar(y_axis, titlex, titley):
    """Function to create a graph"""
    try:
        inicio = time.time()
        ax = plt.subplot()
        plt.xlabel(titlex)
        plt.ylabel(titley)
        plt.title(titlex + " y "+titley)
        ax.plot(y_axis)
        fin = time.time()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        plt.savefig(titlex+titley+".png")
        
    except (KeyboardInterrupt, BufferError):
        fin = time.time()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
    
def convert_tuple(tup):
    """Convert tuples to strings"""
        # initialize an empty string
    stri = ''
    for item in tup:
        stri = stri + str(item)
    return stri
    
def isPrime(n):
    """Check if number is prime"""
     
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

def logic(array):
        dec = int(array,2)
        if(isPrime(dec)):
            return array, dec

def permutaciones(bit):
    """Create all permutation possible for n bits"""
    
    in_file=open("Practica2/permutaciones.txt", "w")
    in_file.write("L{e\n")
    inicio = time.time()
    i = 0
    num_unos = []
    num_digitos = []
    
    while(i < bit):
        
        liminf = 2**i
        limsup = (2**(i+1))
        limmed = math.floor(limsup/4)
        unos = 0
        
        try:
            subsets = list(itertools.islice(itertools.product(*[[0,1]]*(i+1)), liminf, limmed))
            in_file.write(","+' '.join(map(str, subsets)))
            unos += sum(map(sum, subsets))
            #print(subsets)
            del subsets
            
            subsets = list(itertools.islice(itertools.product(*[[0,1]]*(i+1)), limmed, (limmed*2)))
            in_file.write(' '.join(map(str, subsets)))
            unos += sum(map(sum, subsets))
            #print(subsets)
            del subsets
            
            subsets = list(itertools.islice(itertools.product(*[[0,1]]*(i+1)), (limmed*2), (limmed*3)))
            in_file.write(' '.join(map(str, subsets)))
            unos += sum(map(sum, subsets))
            #print(subsets)
            del subsets
            
            subsets = list(itertools.islice(itertools.product(*[[0,1]]*(i+1)), (limmed*3), limsup))
            in_file.write(' '.join(map(str, subsets))+"\n")
            unos += sum(map(sum, subsets))
            #print(subsets)
            del subsets
            
            i += 1
            num_unos.append(unos)  
            num_digitos.append(i)     
            del unos
            
        except (KeyboardInterrupt,OverflowError):
            break
    
    in_file.write("}")
    in_file.close()
    print(num_unos)
    
    fin = time.time()
    
    print("El tiempo de ejecucion es: "+str(fin-inicio))
    ingerir(num_unos, num_digitos)
        
            
if __name__ == "__main__":
    """Main function"""
    
    while True:
        print("\nMENU")
        print("1) Modo manual")
        print("2) Modo automatico")
        print("3) Salir")
        aux = int(input("Seleccione una opcion: "))
            
        if aux == 1:
            n = int(input("\nIntroduce n, no mayor a 2e7 ni menor a 2: "))
            if 2e7 < n < 2:
                print("Error, el numero introducido no es valido")
                break
            permutaciones(n)
        elif aux ==2:
            n = random.randrange(2,2e7)
            permutaciones(n)
            
        elif aux == 3:
            exit()    
        
        else:
            print("Error, seleccione una opcion correcta")
            break