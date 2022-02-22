import math
import random
import matplotlib.pyplot as plt
import os
import time
from os import remove

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

def cleartext(out_file, file):
    array=[]
    in_file=open(file, "r")
    while True:
        file_line = in_file.readline()
        if not file_line:
            in_file.close() #cierro el archivo
            break
        array.append(file_line)
        out_file.write(","+file_line.strip('\n'))
    os.remove(file)
    return array

def ingerir():
    
    out_file = open("resultados.txt", "w") #Abre el txt 
    out_file.write("L{e") #escribo info en el txt
    
    combinaciones=cleartext(out_file, "combinaciones.txt")
    
    out_file.write("}\n")
    out_file.write("#1's{e")
    
    unos=cleartext(out_file, "unos.txt")
    
    out_file.write("}\n")
    out_file.write("# de Digitos{e")
    
    largo=cleartext(out_file, "largo.txt")
    
    out_file.write("}\n")
    out_file.close() 

    #graficar(combinaciones, unos, "Combinaciones posibles", "# de unos")
    #graficar(combinaciones, largo, "Combinaciones posibles", "# de digitos")
    
    #graficar(combinaciones, logrec(unos), "Combinaciones posibles log10", "# de unos")
    #graficar(combinaciones, logrec(largo), "Combinaciones posibles log10", "# de digitos")
    
def logrec(array):
    aux=[]
    for i in array:
        aux.append(math.log10(int(i)))
    return aux
    
def graficar(x_axis, y_axis, titlex, titley):
    try:
        inicio = time.time()
        fig, ax = plt.subplots()
        ax.set_ylabel(titley)
        ax.set_title(titlex)
        ax.grid(False);
        ax.plot(x_axis,y_axis)
        ax.autoscale(enable=True, axis='both', tight=None)
        plt.show()
        fin = time.time()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        
    except (KeyboardInterrupt, BufferError):
        fin = time.time()
        print("El tiempo de ejecucion para la grafica: "+titlex+", "+titley+" es: "+str(fin-inicio))
        pass

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
                n = int(input("\nIntroduce n, no mayor a 1000 ni menor a 0: "))
                if 1000 < n < 0:
                    print("Error, el numero introducido no es valido")
                    break
            
            elif aux ==2:
                n = random.randrange(0,1000)
            
            else:
                print("Error, seleccione una opcion correcta")
                break
            
            check = True
            count = 1
            
            filec = open("combinaciones.txt", "w")
            fileu = open("unos.txt", "w")
            filel = open("largo.txt", "w")
            filep = open("primos.txt", "w")
            
            inicio = time.time()
            while check:
                try:
                    cadena = bina(count)
                    if(primo(count)):
                        filep.write(str(cadena.numero)+"--"+ str(count)+" \n")
                    filec.write(str(cadena.numero)+"\n")
                    fileu.write(str(cadena.numero_de_1)+"\n")
                    filel.write(str(cadena.largo)+"\n")
                    count += 1
                    check = cadena.numero_de_1 != n
                    del cadena
                    
                except BufferError:
                    filec.close()
                    fileu.close()
                    filel.close()
                    filep.close()
                    exit()
                    
                except KeyboardInterrupt:
                    break

            fin = time.time()
            filec.close()
            fileu.close()
            filel.close()
            filep.close()
            print("El tiempo de ejecucion para n = "+str(n)+" es: "+str(fin-inicio))
            del inicio
            del fin
            del aux
            del opc
            del n
            del count
            ingerir()
            
            
        elif opc == 2:
            exit()
        
        else:
            print("Error, seleccione una opcion correcta\n")