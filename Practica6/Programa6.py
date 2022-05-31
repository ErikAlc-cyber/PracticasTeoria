import random
import time
import os
from time import sleep

# It's a stack
class Pila(object):
    def __init__(self):
        self.largo = -1
        self.espacios = []

    def final(self):
        """
        If the length of the list is -1, then the list is empty
        :return: The final method returns a boolean value.
        """
        if self.largo == -1:
            return True
        else:
            return False

    def extraer(self):
        """
        It returns the last element of the list, and then removes it from the list
        :return: The value of the last element in the list.
        """
        if self.final():
            return 'e'
        else:
            valor = self.espacios[self.largo]
            self.largo -= 1
            return valor

    def insertar(self, elemento):
        """
        It inserts an element into the array.
        
        :param elemento: The element to be inserted
        """
        self.largo += 1
        self.espacios[self.largo:] = [elemento]

    def revelar(self):
        """
        It takes the length of the string, and then iterates through the string, adding each character to
        a new string, and then returns the new string
        :return: The string of the spaces in the list.
        """
        i = self.largo
        cadena = ''
        while(i>-1):
            cadena += self.espacios[i]
            i -= 1
        return cadena

def DES(cadena, decision):
    """
    It takes a string and a boolean as arguments, and if the boolean is true, it will print the string
    in a way that makes it look like a stack is being used to process the string
    
    :param cadena: The string to be tested
    :param decision: True or False, if True, the program will show the animation, if False, it will show
    the steps of the program
    """
    pila = Pila()
    archivo = open('Practica6/HISPILA.txt', 'w')
    pila.insertar('Zo')
    estado = 'q'
    auxiliar = cadena
    cadena = cadena + ' '
    archivo.write('La cadena es: ' + auxiliar + '\n')
    for simbolo in cadena:
        if auxiliar == '':
            auxiliar = 'e'
        if decision:
            time.sleep(1)
            ANIMACION(estado, auxiliar, pila)
        else:
            print('(%s, %s, %s)' %(estado, auxiliar, pila.revelar()), end='')
        archivo.write('(%s, %s, %s)' %(estado, auxiliar, pila.revelar()))
        if estado == 'q':
            if simbolo == '0':
                pila.insertar('X')
            elif simbolo == '1':
                if pila.extraer() == 'Zo':
                    pila.insertar('Zo')
                    break
                estado = 'p'
            else:
                estado='q'
                break
        elif estado == 'p':
            if simbolo == '1':
                if pila.extraer() == 'Zo':
                    estado = 'f'
                    pila.insertar('Zo')
                    break
            elif simbolo == '0':
                pila.insertar('X')
                auxiliar = auxiliar[1:]
                break
            elif simbolo == ' ':
                estado = 'f'
            else:
                break
        auxiliar = auxiliar[1:]
        archivo.write('->')

    if auxiliar == '':
        auxiliar = 'e'
    if (pila.revelar() == 'Zo') and auxiliar == 'e' and estado=='f':
        if decision:
            time.sleep(1)
            ANIMACION(estado, auxiliar, pila)
        else:
            print('(%s, %s, %s)' %(estado, auxiliar, pila.revelar()))
            print('\n')
        archivo.write('(%s, %s, %s)' %(estado, auxiliar, pila.revelar()))
        print('Esta cadena es valida')
        archivo.write('\nEsta cadena es valida')
    else:
        print('Esta cadena no es valida')
        archivo.write('\nEsta cadena no es valida')
    archivo.close()

def ANIMACION(estado, cadena_aux, stack):
    """
    It clears the screen, prints the current state, the current string, and the current stack, and then
    waits for 0.9 seconds
    
    :param estado: The current state of the automaton
    :param cadena_aux: The string that is being processed
    :param stack: is the stack that is used in the program
    """
    
    pila = 'Zo'    
    if stack.revelar() != '':
        pila = stack.revelar()
    if os.name =="nt": 
        os.system("cls") 
    else: 
        os.system("clear")
        
    print("\n")
    print(cadena_aux + " -> " +estado+" -> " + pila)
    sleep(0.9)

if __name__ == "__main__":
    
    while True:
        
        print("\n*****PROGRAMA 6: PILA*****")
        print("1.-Colocar la cadena")
        print("2.-Cadena aleatoria")
        print("3.-Salir")
        OP = int(input("Elija una opcion: "))
            
        if OP == 1:
            cadena = input("Escribe el numero binario: ")
        elif OP ==2:
            i = 0
            LONGITUD = random.randint(1, 100000)
            cadena = ''
            while i < LONGITUD:
                cadena += random.choice(['0', '1'])
                i += 1   
        elif OP ==3:
            print("Adios!!\n")
            exit()
        else:
            print("No existe esa opcion\n")
            break
        
        print("El numero es: ", cadena)
        largo = len(cadena)
        if largo <= 10:
            animacion = True
        else:
            print("No se puede realizar la animacion\n")
            animacion = False
            
        DES(cadena, animacion)