import random
import os
from time import sleep

def Maquina (cad, anim):
    """
    It takes a string and a boolean as input, and returns a string
    
    :param cad: The string to be processed
    :param anim: True or False, if you want to see the animation or not
    """
    estado=1
    j=0
    archivo = open("Practica7/MT.txt", "w+")
    while(True):
        try:
            archivo.write(''.join(cad) + " " + str(estado))
            archivo.write("\n")
            if(anim):
                animacion(''.join(cad), j)
            if (estado == 1):
                if(cad[j] == '*'):
                    cad[j] = 'X'
                    j+=1
                    estado = 2
                continue
            elif (estado == 2):
                if(cad[j]=='*'):
                    j+=1
                    estado= 3
                elif(cad[j]=='|'):
                    j+=1
                    estado =2
                continue
            elif estado == 3:
                if(cad[j]=='*'):
                    cad[j] = 'X'
                    j-=1
                    estado = 4
                elif(cad[j]=='|'):
                    j+=1
                    estado= 3
                continue
            elif estado == 4:
                if(cad[j]=='*'):
                    j-=1
                    estado= 4
                elif(cad[j]=='|'):
                    cad[j] = 'a'
                    j+=1
                    estado=5
                elif(cad[j]=='X'):
                    j+=1
                    estado=7
                continue
            elif estado == 5:
                if(j == (len(cad)-1)):
                    cad.append('|')
                    j-=1
                    estado=6
                elif(cad[j]=='*'):
                    j+=1
                    estado=5
                elif(cad[j]=='|'):
                    j+=1
                    estado=5
                elif(cad[j]=='X'):
                    j+=1
                    estado = 5
                continue
            elif estado == 6:
                if(cad[j]=='*'):
                    j-=1
                    estado=6
                elif(cad[j]=='|'):
                    j-=1
                    estado=6
                elif(cad[j]=='a'):
                    cad[j]='|'
                    j-=1
                    estado=4
                elif(cad[j]=='X'):
                    j-=1
                    estado=6
                continue
            elif estado == 7:
                if(cad[j]=='*'):
                    j+=1
                    estado=8
                elif(cad[j]=='|'):
                    j+=1
                    estado=7
                continue
            elif estado == 8:
                if(j == (len(cad)-1)):
                    cad.append('*')
                    j-=1
                    estado=9
                elif(cad[j]=='|'):
                    j+=1
                    estado=8
                elif(cad[j]=='X'):
                    cad[j]='*'
                    j+=1
                    estado=8
                continue
            elif estado == 9:
                if(cad[j]=='*'):
                    j-=1
                    estado=9
                elif(cad[j]=='|'):
                    j-=1
                    estado=9
                elif(cad[j]=='X'):
                    cad[j]='*'
                    estado=9
                    archivo.write(''.join(cad))
                    if(anim):
                        animacion(''.join(cad), j)
                    break
                continue
            else:
                print("Error") 
                break  
        
        except IndexError:
            break
        
    print("La cadena final es: "+''.join(cad))
    
def animacion(cadena, posicion):
    """
    It prints the string, then prints a caret at the position specified.
    
    :param cadena: The string to be animated
    :param posicion: The position of the caret
    """
    animac = []
    if os.name =="nt": 
        os.system("cls") 
    else: 
        os.system("clear") 
    print(cadena)
    for i in range(posicion-1):
        animac.append(" ")
    animac.append("^")
    print(''.join(animac))
    sleep(0.09)        
    
if __name__ == "__main__":
    
    while True:
        
        print("\n*****PROGRAMA 7: MAQUINA DE TURING*****")
        print("1.-Manual")
        print("2.-Automatico")
        print("3.-Salir")
        OP = int(input("Elija una opcion: "))    
        if OP==1:
            n = int( input("Cual es el valor de n: "))
            m = int(input("Cual es el valor de m: "))
        
        elif OP==2:
            n = random.randint(1, 50)
            m = random.randint(1, 50)   
        
        elif OP==3:
            print("Adios!!\n")
            exit()
        
        else:
            print("No existe esa opcion\n")
            break
        
        cad = []
        aux = []
        aux_2 = []
        for i in range (n):
            aux.append('|')
        for i in range (m):
            aux_2.append('|')
             
        cad = list('*'+ ''.join(aux) + '*' + ''.join(aux_2) + '*')
        print("Cadena original: "+ ''.join(cad))
        largo = len(cad)
        if largo <= 10:
            animaniac = True
        else:
            print("No se puede realizar la animacion\n")
            animaniac = False
        Maquina(cad, animaniac)