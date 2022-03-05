import math
import random
import matplotlib.pyplot as plt
import os
import sys
import time
 
clean_nums = [] 

def digest():
    
    global clean_nums
    
    for i in clean_nums:
        print(i)
 
def binary_strings(n, arr, i):
 
    if i == n:
        global clean_nums
        clean_nums.append(''.join(str(e) for e in arr).lstrip("0"))
        return
     
    arr[i] = 0
    binary_strings(n, arr, i + 1)
 
    arr[i] = 1
    binary_strings(n, arr, i + 1)
 
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
                n = int(float(input("\nIntroduce n, no mayor a 2e7 ni menor a 2: ")))
                if 2e7 < n < 2:
                    print("Error, el numero introducido no es valido")
                    break
            
            elif aux ==2:
                n = random.randint(1,2e7)
            
            else:
                print("Error, seleccione una opcion correcta")
                break
            
            inicio = time.time()
            arr = [None] * n
            binary_strings(n, arr, 0)
            fin = time.time()
            
            print("El tiempo de ejecucion para n = "+str(n)+" es: "+str(fin-inicio))
            digest()
            
            
            
        elif opc == 2:
            exit()
        
        else:
            print("Error, seleccione una opcion correcta\n")