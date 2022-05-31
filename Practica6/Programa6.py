import random
import time

class Pila(object):
    def __init__(self):
        self.largo = -1
        self.espacios = []

    def final(self):
        if self.largo == -1:
            return True
        else:
            return False

    def extraer(self):
        if self.final():
            return 'e'
        else:
            valor = self.espacios[self.largo]
            self.largo -= 1
            return valor

    def insertar(self, elemento):
        self.largo += 1
        self.espacios[self.largo:] = [elemento]

    def revelar(self):
        i = self.largo
        cadena = ''
        while(i>-1):
            cadena += self.espacios[i]
            i -= 1
        return cadena

def MANUAL():    
    cadena = input("Escribe el numero binario: ")
    largo = len(cadena)
    if largo <= 10:
        animacion = True
    else:
        print("No se puede realizar la animacion\n")
        animacion = False
        
    DES(cadena, animacion)    
    
def AUTOMATICO():
    i = 0
    LONGITUD = random.randint(1, 100000)
    cadbin = ''
    while i < LONGITUD:
        cadbin += random.choice(['0', '1'])
        i += 1

    print("El numero aleatorio es: ", cadbin)
    largo = len(cadbin)
    if largo <= 10:
        animacion = True
    else:
        print("No se puede realizar la animacion\n")
        animacion = False
        
    DES(cadbin, animacion)
    

def DES(cadena, decision):
    pila = Pila()
    archivo = open('HISPILA.txt', 'w')
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
    
    pila = 'Zo'    
    if stack.revelar() != '':
        pila = stack.revelar()
    
    print("\n")
    print('     %s' %cadena_aux)
    print('     ^')
    print('     |')
    print('     |')
    print('     |')
    print('-----------')
    print('|         |')
    print('|    %s    |' %estado)
    print('|         |')
    print('-----------')
    print('     |')
    print('     |')
    print('     |')
    print('     v')
    print('     %s' %pila)
    print("\n")

if __name__ == "__main__":
    
    while True:
        
        print("\n*****PROGRAMA 6: PILA*****")
        print("1.-Colocar la cadena")
        print("2.-Cadena aleatoria")
        print("3.-Salir")
        OP = int(input("Elija una opcion: "))
            
        if OP == 1:
            MANUAL()
        elif OP ==2:
            AUTOMATICO()   
        elif OP ==3:
            print("Adios!!\n")
            break
        else:
            print("No existe esa opcion\n")
            break
