def MANUAL():
    fin = 0
    estado = 1
    i=0
    j=0
    res= ''
    cad = []
    n = int( input("Cual es el valor de n:"))
    m = int(input("Cual es el valor de m:"))
    aux = ''
    aux_2 = ''
    for i in range (n):
        aux += '|'
    for i in range (m):
        aux_2 += '|'
    
    cad = list('*'+ aux + '*' + aux_2 + '*')
    print("Cadena original: "+ ''.join(cad))
    
    while(fin != 1):
        try:
            if (estado == 1):
                if(cad[j] == '*'):
                    cad[j] = 'X'
                    j+=1
                    estado = 2
                else:
                    print("Primer error")
                continue
            elif (estado == 2):
                if(cad[j]=='*'):
                    j+=1
                    estado= 3
                elif(cad[j]=='|'):
                    j+=1
                    estado =2
                else:
                    print("Error 2")
                continue
            elif estado == 3:
                if(cad[j]=='*'):
                    cad[j] = 'X'
                    j-=1
                    estado = 4
                elif(cad[j]=='|'):
                    j+=1
                    estado= 3
                else:
                    print("Error 3")
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
                else:
                    print("Error 4")
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
                else:
                    print("Error 5")
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
                else:
                    print("Error 6")
                continue
            elif estado == 7:
                if(cad[j]=='*'):
                    j+=1
                    estado=8
                elif(cad[j]=='|'):
                    j+=1
                    estado=7
                else:
                    print("Error 7")
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
                else:
                    print("Error 8")
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
                    fin = 1
                else:
                    print("Error 9")
                continue
            else:
                print("NO SE SABE QUE ONDA") 
                break  
        
        except IndexError:
            break
    print("La cadena final es: "+''.join(cad))
       
def AUTOMATICO():
    cad = ['|']
    print("La primera forma",cad)
    cad.remove(1)
    cad.insert(0,'Hola')
    print("La segunda forma:",cad)
        
    
if __name__ == "__main__":
    
    while True:
        
        print("\n*****PROGRAMA 7: MAQUINA DE TURING*****")
        print("1.-Manual")
        print("2.-Automatico")
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