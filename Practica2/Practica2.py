import math
import random
import matplotlib.pyplot as plt
import os
import time

class Combinacion:
    def __init__(self, combinacion, numero_de_1, largo):
        self.numero = combinacion
        self.numero_de_1 = numero_de_1
        self.largo = largo
 
def contador(numero):
    unos = 0
    for i in numero:
        unos += int(i)
    return unos
 
def bina(decimal):
        
    binario = 0
    mult = 1

    while decimal != 0:
        binario = binario + decimal % 2 * mult
        decimal //= 2
        mult *= 10
    
    strbinario = str(binario)
    unos = contador(strbinario)
    
    return Combinacion(binario, unos, len(strbinario))

def primo(numero):
    if numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True
    
def logrec(array):
    aux=[]
    for i in array:
        aux.append(math.log10(int(i)))
    return aux
    
def ingerir():
    
    out_file = open("Practica2/primos.txt", "w") #Abre el txt 
    out_file.write("Σ^(0,1) = {ε") #escribo info en el txt
    cleartext(out_file, "Practica2/aux1.txt")
    out_file.write("}\n")  
    
    out_file.write("Σ^E = {ε") #escribo info en el txt
    array = cleartext(out_file, "Practica2/aux2.txt")
    out_file.write("}\n")   
    out_file.close()
    
    return array
  
def cleartext(out_file, file):
    array=[]
    in_file=open(file, "r")
    while True:
        file_line = in_file.readline()
        if not file_line:
            in_file.close() #cierro el archivo
            break
        array.append(file_line)
        out_file.write(" ,"+file_line.strip('\n'))
    os.remove(file)
    return array
    
def graficar(x_axis, y_axis, titlex, titley):
    try:
        inicio = time.time()
        ax = plt.subplot()
        plt.xlabel(titlex)
        plt.ylabel(titley)
        plt.title(titlex + " y "+titley)
        plt.autoscale(True, axis='x', tight=True)
        ax.plot(x_axis, y_axis)
        #plt.setp(ax.get_xticklabels(), rotation=40, ha='right', color='r', fontsize='5')
        fin = time.time()
        plt.tight_layout()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        
    except (KeyboardInterrupt, BufferError):
        fin = time.time()
        plt.show()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))

if __name__ == "__main__":
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
                n = int(input("\nIntroduce n, no mayor a 2e7 ni menor a 2: "))
                if 2e7 < n < 2:
                    print("Error, el numero introducido no es valido")
                    break
            
            elif aux ==2:
                n = random.randrange(2,2e7)
            
            else:
                print("Error, seleccione una opcion correcta")
                break
            
            file1 = open("Practica2/aux1.txt", "w")
            file2 = open("Practica2/aux2.txt", "w")
            lim = int(math.pow(2, n))
            unos = []
            largos = []
            inicio = time.time()
            
            for count in range(lim):
                try:
                    if(primo(count)) and count != 0:
                        cadena = bina(count)
                        file1.write(str(cadena.numero)+" \n")
                        file2.write(str(count)+" \n")
                        unos.append(cadena.numero_de_1)
                        largos.append(cadena.largo)
                        del cadena
                
                except (KeyboardInterrupt,BufferError):
                    file1.close()
                    file2.close()
                    break

            fin = time.time()
            file1.close()
            file2.close()
            print("El tiempo de ejecucion para n = "+str(n)+" es: "+str(fin-inicio))
            array = ingerir()
            del inicio
            del fin
            del aux
            del lim
            del opc
            del n
            del count
            
            graficar(array, largos, "Cadenas", "# de digitos")
            graficar(array, unos, "Cadenas", "# de unos")
            graficar(array, logrec(largos), "Cadenas", "log10 de # de digitos")
            graficar(array, logrec(unos), "Cadenas", "log10 de # de unos")
            
            del largos
            del unos
            del array
            
        elif opc == 2:
            exit()
        
        else:
            print("Error, seleccione una opcion correcta\n")